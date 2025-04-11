import { dbase } from './dbase.js';
document.addEventListener('DOMContentLoaded', () => {
    const products = dbase;

    const productList = document.getElementById('products');
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.className = 'product';
        productDiv.innerHTML = `
            <h3>${product.name}</h3>
            <img src = ${product.imagen}/>
            <p>Price: $${product.price}</p>
			<p>Color: ${product.color}</p>
            <button onclick="alert('Added to cart')">Add to Cart</button>
        `;
        productList.appendChild(productDiv);
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
