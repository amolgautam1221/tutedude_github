from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

db = client.test

collection = db['flask-tutorial']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = dict(request.form)
        if not form_data.get('name') or not form_data.get('email'):
            raise Exception("Name and Email are required.")
        collection.insert_one(form_data)
        return "Data Submitted Successfully"

    except Exception as e:
        # error -> stay on same page and show error
        return render_template('index.html', error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

