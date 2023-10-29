from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Set your Alpha Vantage API key here
ALPHA_VANTAGE_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_data/<symbol>')
def get_stock_data(symbol):
    if ALPHA_VANTAGE_API_KEY:
        endpoint = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={ALPHA_VANTAGE_API_KEY}"
        response = requests.get(endpoint)
        data = response.json()
        return data
    else:
        return {"error": "Alpha Vantage API key missing."}

if __name__ == '__main__':
    app.run(debug=True)
