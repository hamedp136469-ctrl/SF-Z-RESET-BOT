#!/usr/bin/env python3
"""
Keep Alive Server - Prevents bot from going idle on Replit
"""

from flask import Flask
from threading import Thread
import logging

app = Flask(__name__)

logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return 'SF × Z RESET BOT is alive! 🤖', 200

@app.route('/ping')
def ping():
    return {'status': 'pong', 'message': 'Bot is running'}, 200

def run_server():
    """Run the Flask server on port 8080"""
    try:
        app.run(host='0.0.0.0', port=8080, debug=False)
    except Exception as e:
        logger.error(f"Server error: {e}")

def start_keep_alive():
    """Start the keep-alive server in a separate thread"""
    server_thread = Thread(target=run_server, daemon=True)
    server_thread.start()
    logger.info("✅ Keep-alive server started on port 8080")
    print("✅ Keep-alive server started on port 8080")
