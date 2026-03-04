from PIL import Image, ImageDraw, ImageFont
import os

# Text input from users.
def get_user_input():
    return input("Enter the text you want to convert to handwriting: ")

# Loads the font from the path.
def load_cursive_font(font_path="Bastigan One.ttf", font_size=60):
    try:
        font = ImageFont.truetype(font_path, font_size)
        return font
    except IOError:
        print (f"Error: Font file '{font_path}' not found.")
        return None
    
# Calculates the required image size based on text length.
def calculate_image_size(text, font, padding=40):
    dummy_img = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
    width = text_width + padding
    height = text_height + padding
    return width, height

# Creates a blank image with the specified dimensions.
def create_blank_image(width, height, background_color="white"):
    return Image.new("RGB", (width, height), color=background_color)

# Draws text on the given image using the specified font.
def draw_text_on_image(image, text, font, text_color="black", padding=20):
    draw = ImageDraw.Draw(image)
    draw.text((padding, padding), text, font=font, fill=text_color)
    return image