from telegram.ext import Application, CommandHandler

Token = "7391485656:AAHUDC0_mcb4HhrspSKCB66arD3hwBBBA_4"

# Create the application
app = Application.builder().token(Token).build()

# Command handlers
async def start(update, context):
    await update.message.reply_text("Hello! Welcome to Echo Cipher!")

async def help(update, context):
    await update.message.reply_text("""
        /start -> Welcome to bot!
        /help -> Hey, I am the help command!
        /content -> I am a prototype!
        /virus -> Check out my channel!
    """)

async def content(update, context):
    await update.message.reply_text("We have various viruses!")

async def virus(update, context):
    await update.message.reply_text("Telegram link: https://t.me/Echoxer")

# Register handlers
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(CommandHandler('content', content))
app.add_handler(CommandHandler('virus', virus))

# Run the bot
if __name__ == '__main__':
    app.run_polling()