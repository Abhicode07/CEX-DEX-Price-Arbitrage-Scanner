from flask import Flask, jsonify
from arbitrage_scanner import get_binance_price, get_solana_price

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """
    Home route to provide basic information about the API.
    """
    return jsonify({
        "message": "Welcome to the Arbitrage Scanner API!",
        "endpoints": {
            "/arbitrage": "Get arbitrage opportunities for predefined trading pairs."
        }
    })

@app.route('/arbitrage', methods=['GET'])
def arbitrage_data():
    """
    Fetch arbitrage data for predefined trading pairs.
    """
    # Define the pairs to analyze
    pairs = [('DOGE/USDC', 'DOGE-USDC')]
    results = []

    try:
        # Iterate through pairs and fetch arbitrage data
        for binance_pair, solana_pair in pairs:
            binance_price = get_binance_price(binance_pair)
            solana_price = get_solana_price(solana_pair)
            
            if binance_price and solana_price:
                # Calculate the arbitrage opportunity
                binance_fee = 0.001
                solana_fee = 0.003
                binance_price_after_fee = binance_price * (1 - binance_fee)
                solana_price_after_fee = solana_price * (1 - solana_fee)
                price_diff_percent = ((solana_price_after_fee - binance_price_after_fee) / binance_price_after_fee) * 100
                
                # Append result
                results.append({
                    'pair': binance_pair,
                    'binance_price': round(binance_price, 8),
                    'solana_price': round(solana_price, 8),
                    'difference_percent': round(price_diff_percent, 2),
                    'arbitrage_opportunity': price_diff_percent > 0
                })
            else:
                results.append({
                    'pair': binance_pair,
                    'error': "Could not fetch prices for this pair."
                })

        # Re-order to ensure solana_price comes after binance_price in the response
        results = [
            {
                'pair': result['pair'],
                'binance_price': result['binance_price'],
                'solana_price': result['solana_price'],
                'difference_percent': result['difference_percent'],
                'arbitrage_opportunity': result['arbitrage_opportunity']
            } for result in results
        ]

        return jsonify({"success": True, "data": results})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
