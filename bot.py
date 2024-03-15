import cv2
import pytesseract
from telegram.ext import Updater, MessageHandler, filters

# Function to detect text with a black background color from an image
def detect_text(update, context):
    # Get the image file from the message
    photo = update.message.photo[-1].get_file()
    # Download the image file
    photo.download('input_image.jpg')

    # Read the image
    image = cv2.imread('input_image.jpg')

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    # Use pytesseract to extract text
    detected_text = pytesseract.image_to_string(binary_image)

    # Send the detected text back to the user
    update.message.reply_text("Detected Text:\n" + detected_text)

def main():
    # Initialize the Telegram bot
    updater = Updater("7160785140:AAHj-EdLG72nSdOtAmaP5SHzFdHF86RgIWg", use_context=True)
    dp = updater.dispatcher

    # Handle photo messages
    dp.add_handler(MessageHandler(filters.photo, detect_text))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
