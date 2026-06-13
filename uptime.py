#!/usr/bin/env python3
"""
Uptime Monitor - Keeps the bot running forever with auto-restart
"""

import subprocess
import time
import logging
import sys
from datetime import datetime

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

def run_bot_forever():
    """
    Run the bot and restart it if it crashes
    """
    restart_count = 0
    
    print("\n" + "="*70)
    print("🔄 SF × Z RESET BOT - ETERNAL UPTIME MANAGER")
    print("="*70)
    print("\n⏰ Bot will restart automatically if it crashes")
    print("📍 Press Ctrl+C to stop the manager\n")
    
    while True:
        restart_count += 1
        start_time = datetime.now()
        
        print(f"\n{'='*70}")
        print(f"🚀 Restart #{restart_count} - {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*70}\n")
        
        try:
            # Run the bot
            process = subprocess.Popen(
                [sys.executable, "bot_runner.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            
            # Print output in real-time
            while True:
                output = process.stdout.readline()
                if output:
                    print(output.rstrip())
                
                if process.poll() is not None:
                    break
            
            # If bot stopped unexpectedly
            uptime = datetime.now() - start_time
            logger.warning(f"⚠️ Bot crashed after {uptime}")
            print(f"\n⚠️ Bot crashed after {uptime}")
            print(f"🔄 Restarting in 10 seconds...\n")
            time.sleep(10)
            
        except KeyboardInterrupt:
            print(f"\n\n🛑 Uptime manager stopped by user")
            logger.info("🛑 Uptime manager stopped by user")
            print(f"Total restarts: {restart_count - 1}")
            sys.exit(0)
        except Exception as e:
            logger.error(f"Error running bot: {e}")
            print(f"\n❌ Error: {e}")
            print(f"🔄 Restarting in 10 seconds...\n")
            time.sleep(10)

if __name__ == "__main__":
    run_bot_forever()
