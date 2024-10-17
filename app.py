from flask import Flask, request, jsonify
import requests

API_KEY = "062c909651716a27a5d7e547"
BASE_URL = f"https://v6.exchangerate-api.com/v6/062c909651716a27a5d7e547/latest/"

app = Flask(__name__)

# Route for home page (with HTML and CSS)
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currency Converter</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .converter-box {
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                max-width: 300px;
                width: 100%;
            }
            h1 {
                text-align: center;
                color: #444;
            }
            form {
                display: flex;
                flex-direction: column;
                gap: 10px;
            }
            label {
                font-size: 1.2em;
            }
            input, select {
                padding: 8px;
                font-size: 1em;
                border-radius: 4px;
                border: 1px solid #ccc;
            }
            button {
                padding: 10px;
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 1.1em;
                cursor: pointer;
            }
            button:hover {
                background-color: #218838;
            }
            .result {
                margin-top: 15px;
                font-size: 1.2em;
            }
        </style>
    </head>
    <body>
        <div class="converter-box">
            <h1>Currency Converter</h1>
            <form id="converter-form">
                <label for="base">Base Currency:</label>
                <select id="base" name="base" required>
                    <option value="USD">USD - US Dollar</option>
                    <option value="EUR">EUR - Euro</option>
                    <option value="GBP">GBP - British Pound</option>
                    <option value="JPY">JPY - Japanese Yen</option>
                    <option value="AUD">AUD - Australian Dollar</option>
                    <option value="INR">INR - Indian Rupee</option>
                    <option value="CAD">CAD - Canadian Dollar</option>
                    <option value="CHF">CHF - Swiss Franc</option>
                    <option value="CNY">CNY - Chinese Yuan</option>
                    <option value="NZD">NZD - New Zealand Dollar</option>
                    <option value="ZAR">ZAR - South African Rand</option>
                </select>

                <label for="target">Target Currency:</label>
                <select id="target" name="target" required>
                    <option value="EUR">EUR - Euro</option>
                    <option value="USD">USD - US Dollar</option>
                    <option value="GBP">GBP - British Pound</option>
                    <option value="JPY">JPY - Japanese Yen</option>
                    <option value="AUD">AUD - Australian Dollar</option>
                    <option value="INR">INR - Indian Rupee</option>
                    <option value="CAD">CAD - Canadian Dollar</option>
                    <option value="CHF">CHF - Swiss Franc</option>
                    <option value="CNY">CNY - Chinese Yuan</option>
                    <option value="NZD">NZD - New Zealand Dollar</option>
                    <option value="ZAR">ZAR - South African Rand</option>
                </select>

                <label for="amount">Amount:</label>
                <input type="number" id="amount" name="amount" placeholder="e.g., 100" required>

                <button type="submit">Convert</button>
            </form>
            <div class="result" id="result"></div>
        </div>

        <script>
            document.getElementById('converter-form').addEventListener('submit', function(e) {
                e.preventDefault(); // Prevent the default form submission

                // Get form values
                const base = document.getElementById('base').value;
                const target = document.getElementById('target').value;
                const amount = document.getElementById('amount').value;

                // Make an API request to the Flask backend
                fetch(`/convert?base=${base}&target=${target}&amount=${amount}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById('result').textContent = data.error;
                    } else {
                        const resultText = `${data.amount} ${data.base_currency} = ${data.converted_amount.toFixed(2)} ${data.target_currency} (Rate: ${data.exchange_rate})`;
                        document.getElementById('result').textContent = resultText;
                    }
                })
                .catch(error => {
                    document.getElementById('result').textContent = 'An error occurred during conversion.';
                    console.error('Error:', error);
                });
            });
        </script>
    </body>
    </html>
    '''

# Route for conversion logic
@app.route('/convert')
def convert_currency():
    base = request.args.get('base', default='USD')  # Get base currency from the request
    target = request.args.get('target', default='EUR')  # Get target currency from the request
    amount = request.args.get('amount', type=float, default=1.0)  # Get amount to convert

    # Construct the API URL for the request
    url = f'{BASE_URL}{base}'
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch exchange rates"}), 500

    data = response.json()

    # Get the conversion rate for the target currency
    rate = data['conversion_rates'].get(target)
    
    if rate is None:
        return jsonify({"error": "Invalid target currency"}), 400

    # Calculate the converted amount
    converted_amount = amount * rate
    
    return jsonify({
        "base_currency": base,
        "target_currency": target,
        "exchange_rate": rate,
        "amount": amount,
        "converted_amount": converted_amount
    })


if __name__ == '__main__':
    app.run(debug=True)