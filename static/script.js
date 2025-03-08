document.addEventListener('DOMContentLoaded', () => {
    const products = [
        { id: 1, name: 'Product 1', price: 10.99 },
        { id: 2, name: 'Product 2', price: 14.99 },
        { id: 3, name: 'Product 3', price: 7.99 }
    ];

    const productsContainer = document.getElementById('products');

    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.className = 'product';
        productDiv.innerHTML = `
            <h3>${product.name}</h3>
            <p>Price: $${product.price}</p>
        `;
        productsContainer.appendChild(productDiv);
    });

    const reviewForm = document.getElementById('review-form');
    reviewForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const reviewText = document.getElementById('review-text').value;
        if (reviewText.trim() !== '') {
            addReview(reviewText);
            document.getElementById('review-text').value = '';
        }
    });

    function addReview(text) {
        const reviewList = document.getElementById('review-list');
        const reviewItem = document.createElement('li');
        reviewItem.textContent = text;
        reviewList.appendChild(reviewItem);

        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ review: text })
        })
        .then(response => response.json())
        .then(data => {
            const sentiment = document.createElement('span');
            sentiment.textContent = ` (Sentiment: ${data.sentiment})`;
            reviewItem.appendChild(sentiment);
        });
    }
});

