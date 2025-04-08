from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import database as db, json
from os import system as sy

app = Flask(__name__)

# Route for home page
@app.route("/")
def home():
	db.from_db()
	db.for_catalog()
	return render_template('index.html')

# Route for product catalog
@app.route("/catalog")
def transactions():
	return render_template("catalog.html", catalog=db.from_db())

# Route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for user registration
@app.route('/register')
def register():
    return render_template('register.html')

# Route for order tracking
@app.route('/order_tracking')
def order_tracking():
    return render_template('order_tracking.html')

# Sentiment analysis endpoint
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    review = data['review']
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return jsonify({'sentiment': sentiment})


if __name__ == '__main__':
    app.run(debug=True)

