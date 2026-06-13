"""
Configuration file for SF × Z RESET BOT
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "8990935337:AAGvvtZZ9DAgdoJ1n7TXYdYAaKFroiGHwps")
ADMIN_ID = int(os.getenv("ADMIN_ID", "8878678556"))

# Rate Limiting
MAX_ATTEMPTS = int(os.getenv("MAX_ATTEMPTS", "3"))
RATE_LIMIT_SECONDS = int(os.getenv("RATE_LIMIT_SECONDS", "5"))

# Instagram API
INSTAGRAM_RESET_URL = "https://www.instagram.com/api/v1/accounts/account_recovery_send_security_email/"
INSTAGRAM_PASSWORD_RESET_PAGE = "https://instagram.com/accounts/password/reset/"

# Logging
LOG_FILE = "bot.log"
LOG_LEVEL = "INFO"

# Bot Information
BOT_NAME = "SF × Z RESET BOT"
BOT_VERSION = "1.0.0"
BOT_DESCRIPTION = "Instagram Password Reset Service"
