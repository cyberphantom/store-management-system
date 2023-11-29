document.addEventListener('DOMContentLoaded', function() {
    // Load items when the document is ready
    loadItems();

    // Add event listener for the add item form submission
    document.getElementById('addItemForm').addEventListener('submit', addItem);
});

function loadItems() {
    fetch('/items')
        .then(response => response.json())
        .then(items => {
            const itemsList = document.getElementById('itemsList');
            itemsList.innerHTML = '';
            items.forEach(item => {
                const itemElement = document.createElement('div');
                itemElement.innerText = `Name: ${item.name}, Quantity: ${item.quantity}`;
                itemsList.appendChild(itemElement);
            });
        })
        .catch(error => console.error('Error:', error));
}

function addItem(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const item = Object.fromEntries(formData.entries());
    
    fetch('/items/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(item),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        loadItems(); // Reload items to update the list
    })
    .catch(error => console.error('Error:', error));

    event.target.reset(); // Reset form after submission
}
