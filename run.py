import hashlib
import os
import random
import time
import logging
import cloudscraper
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

requests = cloudscraper.create_scraper()
requests.headers = {
    "Authorization": os.getenv("TOKEN"),
}

def click_button():
    url = "https://discord.com/api/v9/interactions"
    payloads = {
        "type": 3,  # Button interaction type
        "guild_id": os.getenv("GUILD_ID"),
        "channel_id": os.getenv("CHANNEL_ID"),
        "message_id": os.getenv("MESSAGE_ID"),  # ID pesan yang berisi tombol
        "application_id": os.getenv("APPLICATION_ID"),
        "session_id": hashlib.md5(str(random.randint(1, 99999999999999)).encode()).hexdigest(),
        "data": {
            "component_type": 2,  # Button component
            "custom_id": os.getenv("CUSTOM_ID")  # Custom ID dari tombol yang mau diklik
        },
        "nonce": str(random.randint(1, 99999999999999))
    }
    
    try:
        r = requests.post(url, json=payloads)
        r.raise_for_status()
        logging.info(f"Button clicked successfully with status code: {r.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")

while True:
    click_button()
    sleep_time = random.randint(7200, 7800)  # 2 jam ± beberapa menit
    logging.info(f"Sleeping for {sleep_time} seconds ({sleep_time/3600:.2f} hours)")
    time.sleep(sleep_time)
