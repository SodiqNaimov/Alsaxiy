import telebot
from telebot import types
from fpdf import FPDF
import os
# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = '5828429572:AAF-v2yuP5N3X9o6TnoJCWS6hJmT0Q2nZSg'
bot = telebot.TeleBot(TOKEN)


# Handler for /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the CV bot! Please provide your name.")


# Handler for receiving name
@bot.message_handler(func=lambda message: True)
def ask_for_photo(message):
    bot.reply_to(message, "Thanks, now please send me your photo.")
    bot.register_next_step_handler(message, save_name)


# Handler for receiving photo
def save_name(message):
    name = message.text
    if message.photo:
        photo_id = message.photo[-1].file_id
        # Here you would save the name and photo to a database or storage
        # and then create the PDF CV using that information
        create_pdf_cv(name, photo_id, message.chat.id)
    else:
        bot.reply_to(message, "Please send a photo.")


# Function to create PDF CV
def create_pdf_cv(name, photo_id, chat_id):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add name to the PDF
    pdf.cell(200, 10, txt=f"Name: Sodiq", ln=True, align="L")

    # Add photo to the PDF (You may want to handle photos differently)
    photo_url = bot.get_file(photo_id).file_path
    photo_file = bot.download_file(photo_url)
    with open("photo.jpg", "wb") as photo:
        photo.write(photo_file)
    pdf.image("photo.jpg", x=10, y=20, w=40)

    # Save the PDF with user's chat_id as filename
    pdf_file_name = f"{chat_id}_CV.pdf"
    pdf.output(pdf_file_name)

    # Send the PDF to the user
    with open(pdf_file_name, "rb") as pdf_file:
        bot.send_document(chat_id, pdf_file)

    # Clean up
    os.remove(pdf_file_name)
    os.remove("photo.jpg")


# Polling loop
bot.polling()
