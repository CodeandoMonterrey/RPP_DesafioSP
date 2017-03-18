from flask import Flask, request
import requests
app = Flask(__name__)

def get_sentiment(text):
    data = requests.get("https://damp-spire-78293.herokuapp.com/sentiment?text="+text)
    return(data.json()["value"])

@app.route("/")
def hello():
    text = str(request.args.get('text'))
    response = get_sentiment(text)
    return str(response)

if __name__ == "__main__":
    app.run()
