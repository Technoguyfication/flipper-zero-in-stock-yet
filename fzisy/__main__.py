import logging
import signal
import time
import requests

from bs4 import BeautifulSoup
from twilio.rest import Client

from .config import Config

FLIPPER_ZERO_URL = "https://shop.flipperzero.one/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

running = True

def main():
    config = Config()

    # Set up logging
    logging.basicConfig(level=config.log_level)

    # Validate config
    valid, error = config.validate()
    if not valid:
        logging.error(f"Failed to load config: {error}")
        return

    twilio_client = Client(config.twilio_account_sid, config.twilio_auth_token)

    while running:

        logging.info("Checking if item is in stock...")

        # Check if item is in stock
        if check_availability():
            logging.info("Item is in stock!")

            # Send message to each number in the broadcast list
            for number in config._sms_broadcast_list:
                twilio_client.messages.create(
                    to=number,
                    from_=config.twilio_from_number,
                    body=f"The Flipper Zero is in stock!\n\n{FLIPPER_ZERO_URL}"
                )
            
            # Pause for one hour before checking again
            time.sleep(3600)
        else:
            logging.info("Item is not in stock")

            # Pause for 10 minutes before checking again
            time.sleep(600)

def check_availability():
    response = requests.get(FLIPPER_ZERO_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    # Recursively find all <div> elements with class="featured-product__price"
    featured_prices = soup.find_all('div', class_='featured-product__price', recursive=True)

    # Check that none of the child elements of each <div> contain the text "Sold Out"
    for price in featured_prices:
        if any(child for child in price.descendants if 'sold out' in str(child).lower()):
            return False
    
    return True # If we get here, item is in stock

def handle_signal(signum, frame):
    global running
    running = False

if __name__ == "__main__":

    # Set up signal handlers
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    main()
