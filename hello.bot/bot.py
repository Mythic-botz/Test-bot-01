from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# 🔐 Replace this with your own BotFather token
BOT_TOKEN = "8175393588:AAHQBtIBXBWwnUZrGgNqSeGUAbCCv-stPX8"

# 🟢 This function handles the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Hello! I'm your first Telegram bot!")

# 💬 This function handles normal text messages (not commands)
def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text  # ✍️ The message sent by the user
    update.message.reply_text(f"📩 I received: {user_text}")

# 🚀 Main function to run the bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)  # 🧠 Connect bot using your token
    dp = updater.dispatcher  # 🎛️ Dispatcher handles messages and commands

    # 📌 Add a handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # 📌 Add a handler for normal text messages (not commands)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # ▶️ Start polling Telegram for updates (messages)
    updater.start_polling()

    # ⏳ Keep the bot running until you press Ctrl+C
    updater.idle()

# 🧠 If this file is run directly, start the bot!
if __name__ == '__main__':
    main()
