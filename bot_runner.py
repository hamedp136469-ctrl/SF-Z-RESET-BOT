#!/usr/bin/env python3
"""
Bot Runner - Runs the bot with keep-alive support for Replit
"""

import logging
import sys
from keep_alive import start_keep_alive
from bot import main

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

def main_runner():
    """Main runner function"""
    print("\n" + "="*60)
    print("🚀 SF × Z RESET BOT - STARTING ON REPLIT")
    print("="*60)
    print("\n📌 Starting keep-alive server...")
    
    # Start the keep-alive server
    start_keep_alive()
    
    print("\n🤖 Starting Telegram bot...\n")
    
    try:
        # Start the bot
        main()
    except KeyboardInterrupt:
        logger.info("\n🛑 Bot stopped by user")
        print("\n🛑 Bot stopped.")
        sys.exit(0)
    except Exception as e:
        logger.error(f"\n❌ Fatal error: {e}")
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main_runner()
