from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your simple Telegram bot.")

# Define a function to handle normal messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    # Create an Updater and pass your bot's token
    updater = Updater("7160785140:AAHj-EdLG72nSdOtAmaP5SHzFdHF86RgIWg")

    # Get the dispatcher
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register a message handler for all messages
    dp.add_handler(MessageHandler(filters.text & ~filters.command, echo))

    # Start the Bot
    updater.start_polling()

   

