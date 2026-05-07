from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api')
def json_data():
    f = open('data.json', 'r')   
    mydata = json.load(f)         
    f.close()                    

    return jsonify(mydata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
