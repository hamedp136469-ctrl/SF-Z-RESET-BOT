# 🤖 SF × Z RESET BOT - REPLIT FOREVER SETUP

## ✨ Features for Eternal Uptime

This setup ensures your bot runs **forever on Replit** with:

✅ **Keep-Alive Server** - Prevents idle timeout (Flask on port 8080)  
✅ **Auto-Restart Manager** - Restarts bot if it crashes  
✅ **Eternal Uptime** - Never stops unless you manually stop it  
✅ **Real-time Monitoring** - Shows restart counts and uptime  

---

## 🚀 How to Run on Replit

### Option 1: Standard Run (Keep-Alive)

```bash
python bot_runner.py
```

This will:
- Start the Flask keep-alive server (port 8080)
- Start the Telegram bot
- Prevent Replit idle timeout

### Option 2: With Auto-Restart Manager (RECOMMENDED)

```bash
python uptime.py
```

This will:
- Start the bot with keep-alive server
- Auto-restart if bot crashes
- Show real-time restart information
- Keep running forever

### Option 3: Use Replit's Run Button

The `.replit` file is already configured. Just click the **Run** button on Replit!

---

## 📡 How the Keep-Alive Works

Replit will put your app to sleep if it doesn't receive HTTP requests. Our setup:

1. **Flask Server** runs on port 8080
2. **Keeps the server alive** by responding to HTTP requests
3. **Telegram Bot** runs simultaneously in the same process
4. **Both run together** without interfering

---

## 🌐 Access Your Keep-Alive Server

Once running, you can access:

- **Home:** `https://your-replit-url.repl.co/`
- **Ping:** `https://your-replit-url.repl.co/ping`

Example response:
```json
{
  "status": "pong",
  "message": "Bot is running"
}
```

---

## 🔄 Auto-Restart Features

When using `python uptime.py`:

```
======================================================================
Restart #1 - 2026-06-13 14:30:45
======================================================================

🤖 SF × Z RESET BOT - RUNNING
✅ Keep-alive server started on port 8080
Bot is polling for messages...

(if bot crashes...)

⚠️ Bot crashed after 0:15:32
🔄 Restarting in 10 seconds...

======================================================================
Restart #2 - 2026-06-13 14:30:55
======================================================================
```

---

## 📊 Files Explained

| File | Purpose |
|------|----------|
| `.replit` | Replit configuration file |
| `bot.py` | Main Telegram bot |
| `keep_alive.py` | Flask server for preventing timeout |
| `bot_runner.py` | Runs bot + keep-alive server |
| `uptime.py` | Auto-restart manager |
| `requirements.txt` | Python dependencies (updated) |

---

## ⚙️ Configuration

Bot credentials are hardcoded in `bot.py`:

```python
BOT_TOKEN = "8990935337:AAGvvtZZ9DAgdoJ1n7TXYdYAaKFroiGHwps"
ADMIN_ID = 8878678556
```

### To Change:

1. Open `bot.py`
2. Find lines with `BOT_TOKEN` and `ADMIN_ID`
3. Update with your values
4. Save and restart

---

## 🐛 Troubleshooting

### Bot not responding to Telegram

1. Check bot token is correct in `bot.py`
2. Verify bot is running (check console)
3. Test with `/help` command
4. Check admin logs with `/status`

### Keep-alive server not working

1. Check if port 8080 is available
2. Verify Flask is installed: `pip install flask`
3. Check console for error messages

### Bot crashes repeatedly

1. Use `uptime.py` for auto-restart
2. Check `bot.log` file for errors
3. Verify Instagram API is accessible
4. Check Telegram bot token is valid

---

## 📈 Monitoring

### Check Bot Uptime

```bash
# In Replit console
ls -la bot.log
tail -f bot.log
```

### Monitor Keep-Alive

```bash
curl https://your-replit-url.repl.co/ping
```

---

## 🎯 Recommended Setup

1. **Use `python uptime.py`** for true 24/7 uptime
2. **Enable Replit Always-On** for premium accounts (optional)
3. **Monitor via `/status` command** in Telegram
4. **Check logs** regularly for issues

---

## 💡 Tips

- ✅ Keep Replit tab open or upgrade to Always-On
- ✅ Monitor bot performance with `/status`
- ✅ Check logs for any errors
- ✅ Restart periodically (once a week) for stability
- ✅ Keep `keep_alive.py` running at all times

---

## 🚀 Start Now

Run this in Replit console:

```bash
python uptime.py
```

That's it! Your bot will now run **forever** on Replit! 🎉

---

**Made with ❤️ for eternal uptime**
