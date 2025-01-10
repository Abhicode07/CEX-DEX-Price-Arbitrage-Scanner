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
