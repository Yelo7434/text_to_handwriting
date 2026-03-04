from PIL import Image, ImageDraw, ImageFont
import os

#Text input from users.
def get_user_input():
    return input("Enter the text you want to convert to handwriting: ")

#Loads the font from the path.
def load_cursive_font(font_path="Bastigan One.ttf", font_size=60):
    try:
        font = ImageFont.truetype(font_path, font_size)
        return font
    except IOError:
        print (f"Error: Font file '{font_path}' not found.")
        return None
    
    