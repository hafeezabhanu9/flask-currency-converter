# Flask Currency Converter API

This is a simple Flask-based web application for converting currencies using the [ExchangeRate-API](https://www.exchangerate-api.com/). The application allows users to select a base currency, target currency, and input an amount, which will be converted based on the latest exchange rates.

## Features
- Convert currencies between multiple options such as USD, EUR, GBP, JPY, INR, etc.
- Simple web interface with a form to input currencies and amount.
- Exchange rates fetched from the ExchangeRate-API.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework for Python.
- **HTML/CSS**: For the front-end.
- **ExchangeRate-API**: API to get real-time exchange rates.
- **Docker**: Containerization of the application.

## Getting Started

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
- [Docker](https://www.docker.com/get-started)

### Installation and Setup

1. **Clone the repository**:
   - git clone https://github.com/hafeezabhanu9/flask-currency-converter.git
   - cd flask-currency-converter

2. **Install required dependencies**:

- **If running locally, create a virtual environment and install Flask**: pip install Flask requests

3. **Environment Variables**:

- You may want to create a .env file to store sensitive information like your API key (if applicable).

4. **Run the Application**:

- **Start the Flask application**: python app.py
- Navigate to http://127.0.0.1:5000 in your web browser to access the application.

### Docker Setup

- Build the Docker image:
- **In the project directory, run**: docker build -t flask-currency-converter .
- Run the Docker container
- **Execute the following command to run the container**: docker run -d -p 5000:5000 flask-currency-converter
- The application will be accessible at http://localhost:5000

## API Endpoints

### 1. Convert Currency

- **URL**: `/convert`
- **Method**: `GET`
- **Description**: Converts a specified amount from one currency to another using live exchange rates.

#### Query Parameters:

| Parameter  | Type   | Description                                  |
|------------|--------|----------------------------------------------|
| `base`     | string | The base currency code (e.g., `USD`, `EUR`)  |
| `target`   | string | The target currency code (e.g., `INR`, `GBP`)|
| `amount`   | float  | The amount to convert                        |

#### Success Response:

- **Code**: 200 OK
- **Content**:

```json
{
    "base_currency": "USD",
    "target_currency": "INR",
    "exchange_rate": 74.35,
    "amount": 100,
    "converted_amount": 7435.00
}
````

#### Error Response:

- **Code**: 400 BAD REQUEST
- **Content**:
  
``` json
{
    "error": "Invalid currency code or parameters"
}
```

### How it Works
- The API expects valid currency codes (ISO 4217 format, such as USD, EUR, etc.) and a numeric value for the amount.
- The GET /convert endpoint fetches the latest exchange rate from the external service and performs the conversion.
- The response includes the exchange rate used, the base currency, target currency, and the converted amount.
  
### Notes:
- Currency conversion accuracy depends on the rates provided by the external API service.
- Ensure you use valid currency codes; invalid codes will return an error.

## Project Structure

flask-currency-converter/
│
├── app.py              # Main Flask application
├── Dockerfile          # Dockerfile to containerize the app
└── README.md           # Project documentation

## Author
Hafeeza Bhanu Mohmmad

### Acknowledgements
- ExchangeRate-API: For providing the currency conversion service.
- Flask Documentation: For the guidance in building the application.

## License
This project is licensed under the MIT License.
