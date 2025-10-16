from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# Replace with your actual Telegram user ID
ADMIN_ID = 7029072670  

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.forward_message(
        chat_id=ADMIN_ID,
        from_chat_id=update.message.chat_id,
        message_id=update.message.message_id
    )

app = ApplicationBuilder().token("8466147278:AAHZjPsyUTY2Ez3uLqynZpGsIiJP1LIV0j8").build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward))
app.run_polling()