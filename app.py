from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import database as db, json
from os import system as sy

app = Flask(__name__)

#@app.route("/")
#def home():
#    return render_template('index.html')

def from_db():
	cursor = db.connection.cursor()
	cursor.execute("SELECT * FROM productos")
	myresult = cursor.fetchall()
	#Convertir los datos a diccionario
	insertObject = []
	columnNames = [column[0] for column in cursor.description]
	for record in myresult:
		insertObject.append(dict(zip(columnNames, record)))
	cursor.close()
	return insertObject

# Route for home page
@app.route("/")
def get_transactions():
	return render_template("index.html", index=datos)

# Route for product catalog
@app.route("/catalog")
def catalog():
	iden = open("./static/dbase.js", "w")
	iden.write(f"export const dbase = {from_db()}")
	iden.close()
	return render_template('catalog.html')

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

