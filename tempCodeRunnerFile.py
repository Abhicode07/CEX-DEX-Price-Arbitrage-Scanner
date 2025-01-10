import requests
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_binance_price():
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDC'
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        return float(data['price'])
    except Exception as e:
        logging.error(f"Binance error: {e}")
        return None

def get_solana_price():
    # Using Birdeye API for Solana prices
    url = 'https://api.birdeye.so/v1/public/price?address=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'  # USDC address
    headers = {
        'X-API-KEY': '5c3e5eb592334c919b0c656802c2d151'  # Public API key
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()
        return float(data['data']['value'])
    except Exception as e:
        logging.error(f"Solana error: {e}")
        return None

def main():
    while True:
        try:
            binance = get_binance_price()
            solana = get_solana_price()
            
            if binance:
                logging.info(f"Binance DOGE/USDC: {binance:.8f}")
            if solana:
                logging.info(f"Solana DOGE/USDC: {solana:.8f}")
            
            if binance and solana:
                diff_percent = abs(binance - solana) / min(binance, solana) * 100
                logging.info(f"Difference: {diff_percent:.2f}%")
            
            time.sleep(5)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            logging.error(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()