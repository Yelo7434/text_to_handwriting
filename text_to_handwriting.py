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
    
#Calculates the size of the image based on the text and font.
def calculate_image_size(text, font):
    lines = text.split('\n')
    max_line_width = max(font.getsize(line)[0] for line in lines)
    total_height = sum(font.getsize(line)[1] for line in lines) + (len(lines) - 1) * 10
    return (max_line_width + 20, total_height + 20)

