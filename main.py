from typing import Final
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import utils

TOKEN: Final = "6357007065:AAHo8EGSfN6JZX4NDkVnM5c6VivGycTjZnA"

class Prog:
    def __init__(self) -> None:
        self.running: bool = False

prog: Prog = Prog()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prog.running = True
    await context.bot.send_message(chat_id=update.effective_chat.id, text="The bot is running send me a link and I will try my best")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text    
    if prog.running:
        utils.download(text, "")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    prog.running = False
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Stopped bot")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('stop', stop))

    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    application.run_polling(3)
