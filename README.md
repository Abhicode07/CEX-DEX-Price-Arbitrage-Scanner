# CEX-DEX Price Arbitrage Scanner

This is a backend application built with FastAPI to fetch and calculate arbitrage opportunities between Binance and Solana. It provides a RESTful API endpoint to retrieve arbitrage data for specified tokens.

---

## Features

- **Real-Time Data**: Fetches live prices from Binance and Solana.
- **Arbitrage Calculation**: Calculates potential profits with consideration of:
  - Trading fees
  - Slippage
- **API Endpoint**: Exposes data in a structured format for easy integration.

---

## Requirements

- **Python**: Version 3.9+
- **Binance API**: API Key and Secret
- **Solana RPC Endpoint**: Access to Solana blockchain

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>

2. Set Up Virtual Environment
Create and activate a virtual environment:

bash
Copy code
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
3. Install Dependencies
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory with the following keys:

env
Copy code
BINANCE_API_KEY=your_binance_api_key
BINANCE_API_SECRET=your_binance_api_secret

![image](https://github.com/user-attachments/assets/efc3ae7c-d825-44ff-a925-8fb547d7d6b5)
![image](https://github.com/user-attachments/assets/e76cc463-293e-44c4-b876-8b2014c07ecf)

