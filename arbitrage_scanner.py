import requests
import time

def get_solana_price(pair):
    """
    Fetch the price of a token pair from the Raydium API on Solana.
    """
    base, quote = pair.split('-')
    url = f'https://api.raydium.io/v2/main/price?token={base}&vsToken={quote}'
    
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, dict) and len(data) > 0:
            # Return the first price value found
            return float(next(iter(data.values())))
        print(f"Unexpected data structure from Raydium API: {data}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Solana price: {e}")
        return None

def get_binance_price(symbol):
    """
    Fetch the price of a trading pair from the Binance API.
    """
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol.replace("/", "")}'
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return float(data['price']) if 'price' in data else None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Binance price: {e}")
        return None

def calculate_arbitrage(binance_price, solana_price, pair):
    """
    Calculate the arbitrage opportunity between the Binance and Solana prices.
    """
    if not (binance_price and solana_price):
        print(f"Could not fetch price data for {pair}")
        return
    
    binance_fee = 0.001  # 0.1% fee on Binance
    solana_fee = 0.003  # 0.3% fee on Solana
    
    binance_price_after_fee = binance_price * (1 - binance_fee)
    solana_price_after_fee = solana_price * (1 - solana_fee)
    
    price_diff_percent = ((solana_price_after_fee - binance_price_after_fee) / binance_price_after_fee) * 100
    
    print(f"\n{pair} Analysis:")
    print(f"Binance Price: {binance_price:.8f}")
    print(f"Solana Price: {solana_price:.8f}")
    print(f"Difference: {price_diff_percent:.2f}%")
    
    if price_diff_percent > 0:
        print(f"Arbitrage Opportunity: {price_diff_percent:.2f}% profit after fees")
    else:
        print(f"No arbitrage opportunity: {price_diff_percent:.2f}% loss after fees")

def main():
    """
    Main loop that checks for arbitrage opportunities in the specified trading pairs.
    """
    pairs = [('DOGE/USDC', 'DOGE-USDC')]  # Predefined trading pairs
    
    while True:
        try:
            for binance_pair, solana_pair in pairs:
                print(f"\nChecking {binance_pair}...")
                binance_price = get_binance_price(binance_pair)
                solana_price = get_solana_price(solana_pair)
                calculate_arbitrage(binance_price, solana_price, binance_pair)
                time.sleep(1)  # Short delay between checks
            
            time.sleep(10)  # Wait before the next round of checks
            
        except KeyboardInterrupt:
            print("\nStopping arbitrage scanner...")
            break
        except Exception as e:
            print(f"Main loop error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
