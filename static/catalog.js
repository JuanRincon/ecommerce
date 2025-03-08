document.addEventListener('DOMContentLoaded', () => {
    const products = [
        { id: 1, name: 'Electrical Wire', price: 25.99 },
        { id: 2, name: 'Circuit Breaker', price: 45.99 },
        { id: 3, name: 'LED Bulb', price: 5.99 }
    ];

    const productList = document.getElementById('products');
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.innerHTML = `
            <h3>${product.name}</h3>
            <p>Price: $${product.price}</p>
            <button onclick="alert('Added to cart')">Add to Cart</button>
        `;
        productList.appendChild(productDiv);
    });
});

