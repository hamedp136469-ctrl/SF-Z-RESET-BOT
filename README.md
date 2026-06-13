# 🔐 SF × Z RESET BOT

**Instagram Password Reset Service via Telegram**

## 📋 Overview

SF × Z RESET BOT is a professional Telegram bot that helps Instagram users reset their forgotten passwords securely and quickly. The bot sends official password reset emails through Instagram's official channels.

### ✨ Features

✅ **Fast & Reliable** - Quick password reset processing  
✅ **24/7 Available** - Always online to help  
✅ **100% Secure** - Official Instagram integration  
✅ **User-Friendly** - Simple and intuitive interface  
✅ **Input Validation** - Secure username/email verification  
✅ **Admin Logging** - Track all bot activities  
✅ **Rate Limiting** - Prevent abuse with attempt limits  
✅ **Error Handling** - Professional error messages  

---

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Telegram Bot API token

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/hamedp136469-ctrl/SF-Z-RESET-BOT.git
cd SF-Z-RESET-BOT

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your configuration
# Add your BOT_TOKEN and ADMIN_ID
```

### 4. Run the Bot

```bash
python bot.py
```

You should see:
```
==================================================
🤖 SF × Z RESET BOT - RUNNING
==================================================
Token: 8990935337:AAGvvtZZ...
Admin ID: 8878678556
Press Ctrl+C to stop
==================================================
```

---

## 📱 Bot Commands

### Available Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the password reset process |
| `/help` | Show help and usage information |
| `/about` | Information about the bot |
| `/status` | Check current bot and system status |
| `/cancel` | Cancel current operation |

---

## 🎯 How It Works

### Step-by-Step Process

1. **User sends `/start`**
   - Bot displays welcome message with instructions
   - User is prompted to enter Instagram username or email

2. **User enters username or email**
   - Bot validates the input format
   - Bot asks for confirmation

3. **User confirms information**
   - Bot sends reset request to Instagram
   - User receives confirmation message

4. **Password reset email**
   - Instagram sends official password reset email
   - User follows link to reset password

---

## 🔒 Security Features

- ✅ Input validation for usernames and emails
- ✅ Rate limiting to prevent abuse
- ✅ Maximum attempt limits per user
- ✅ Admin logging for all activities
- ✅ Error handling with safe messages
- ✅ No password storage
- ✅ Official Instagram API integration

**Important:** This bot does NOT store passwords or account credentials. It only processes official password reset requests through Instagram's systems.

---

## 📊 Admin Features

### Admin Logging

The bot sends real-time notifications to the configured admin ID:

- 👤 New user started
- ✅ Reset successful
- ❌ Reset failed
- ⚠️ Error occurred
- 📊 System status updates

### Configuration

Set your admin ID in `.env`:
```
ADMIN_ID=8878678556
```

---

## ⚙️ Configuration Options

### Environment Variables

```env
# Required
BOT_TOKEN=your_telegram_bot_token
ADMIN_ID=your_admin_telegram_id

# Optional
MAX_ATTEMPTS=3              # Maximum reset attempts per user
RATE_LIMIT_SECONDS=5        # Rate limit in seconds
LOG_LEVEL=INFO              # Logging level (INFO, DEBUG, WARNING, ERROR)
```

---

## 📝 Example Usage

### User Interaction

```
User: /start

Bot: ╔════════════════════════════════════════╗
     ║   🔐 SF × Z RESET BOT 🔐              ║
     ║   Instagram Password Reset Service    ║
     ╚════════════════════════════════════════╝
     
     👋 Welcome, John!
     
     🎯 What This Bot Does:
     • Sends official Instagram password reset emails
     • Fast & Secure process
     • Works 24/7
     
     📝 Please enter your Instagram username or email

User: john_doe

Bot: 🔍 Confirm Your Information
     📧 Input Type: Username
     john_doe
     
     Is this correct?

User: ✅ Yes, Continue

Bot: ✅ Success! Password Reset Email Sent
     📧 We've sent a password reset email...
```

---

## 🛠️ Development

### Project Structure

```
SF-Z-RESET-BOT/
├── bot.py              # Main bot application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment file
├── .gitignore          # Git ignore file
├── LICENSE             # MIT License
└── README.md           # This file
```

### Running in Development Mode

```bash
# Enable debug logging
export LOG_LEVEL=DEBUG
python bot.py
```

---

## 📦 Dependencies

- **python-telegram-bot** (20.7) - Telegram Bot API wrapper
- **aiohttp** (3.9.1) - Async HTTP client
- **python-dotenv** (1.0.0) - Environment variable management
- **requests** (2.31.0) - HTTP library

---

## 🐛 Troubleshooting

### Bot Not Responding

1. Check if bot token is correct
2. Verify internet connection
3. Check bot logs: `tail -f bot.log`
4. Ensure bot is running: `python bot.py`

### Not Receiving Reset Emails

1. Check spam/promotions folder
2. Verify email address associated with Instagram
3. Wait 5-10 minutes for email delivery
4. Try visiting: https://instagram.com/accounts/password/reset/

### Rate Limit Issues

- Bot enforces maximum 3 attempts per user
- Wait before attempting again
- Contact admin for issues

---

## 📞 Support

### Help & Resources

- 📚 [Telegram Bot Documentation](https://core.telegram.org/bots/api)
- 📞 [Instagram Help Center](https://help.instagram.com/)
- 🔗 [Direct Reset Page](https://instagram.com/accounts/password/reset/)

### Contact

For issues or feedback, please reach out to the admin.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

**Important:** This bot is designed to help users reset their own Instagram passwords only. Users must:

- Only use this bot for their own accounts
- Never use it to access others' accounts
- Follow Instagram's terms of service
- Use only legitimate reset requests

Misuse of this bot may result in account suspension or legal consequences.

---

## 🎉 About

**SF × Z RESET BOT v1.0.0**

A professional Telegram bot for Instagram password resets. Built with ❤️ for security and ease of use.

© 2024 SF × Z RESET BOT. All rights reserved.

---

## 🌟 Features Coming Soon

- [ ] Multiple language support
- [ ] Account recovery options
- [ ] Two-factor authentication help
- [ ] Statistics dashboard
- [ ] Advanced admin controls
- [ ] User feedback system

---

**Made with ❤️ by SF × Z Team**
