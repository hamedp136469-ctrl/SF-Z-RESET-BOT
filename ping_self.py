#!/usr/bin/env python3
"""
Self-Ping Script - Pings Replit every 5 minutes to keep it alive
"""

import os
import requests
import time
import logging
from threading import Thread

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

def get_replit_url():
    """Get Replit URL from environment"""
    # On Replit, the URL is available in the REPLIT_SLUG environment variable
    slug = os.getenv("REPLIT_SLUG")
    owner = os.getenv("REPLIT_OWNER")
    
    if slug and owner:
        return f"https://{slug}.{owner}.repl.co"
    
    # Fallback
    return os.getenv("REPLIT_URL", "http://localhost:8080")

def ping_loop():
    """Ping the server every 5 minutes"""
    url = get_replit_url()
    logger.info(f"🔔 Self-ping enabled for: {url}")
    print(f"🔔 Self-ping enabled for: {url}")
    
    while True:
        try:
            time.sleep(300)  # Wait 5 minutes
            response = requests.get(f"{url}/ping", timeout=10)
            if response.status_code == 200:
                logger.info("✅ Self-ping successful")
            else:
                logger.warning(f"⚠️ Self-ping returned status {response.status_code}")
        except Exception as e:
            logger.warning(f"⚠️ Self-ping failed: {e}")

def start_self_ping():
    """Start self-ping in a background thread"""
    ping_thread = Thread(target=ping_loop, daemon=True)
    ping_thread.start()
    logger.info("✅ Self-ping thread started")
    print("✅ Self-ping thread started")
