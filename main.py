# Import necessary libraries
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
from random import randint

# Set the output path and watermark text
OUTPUT_PATH = r".\static\done_watermarking\image_with_watermark.png"
WATERMARK_TEXT = "Official_Beast"
original_img_path = ""

# Create the main Tkinter window
window = Tk()
window.minsize(width=500, height=500)
window.title("Image-Watermarking")

# Function to browse and select an image file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        global original_img_path
        original_img_path = file_path

# Function to insert watermark into the image
def insert_watermark(input_image_path, output_image_path, watermark_text, font_size=36):
    # Open the original image
    original_image = Image.open(input_image_path)

    # Create a transparent image for the watermark
    watermark = Image.new("RGBA", original_image.size, (255, 255, 255, 0))

    # Choose a font and size for the watermark
    font = ImageFont.truetype("./font\LoveDays-2v7Oe.ttf", font_size)

    # Create a drawing context for the watermark
    draw = ImageDraw.Draw(watermark)

    # Calculate the size of the watermark text
    text_size = draw.textbbox((0, 0), watermark_text, font)

    for i in range(6):
        width_plus = randint(0, 6)
        height_plus = randint(0, 6)
        print(width_plus, height_plus)
        # Calculate the position to center the watermark on the image
        x = (original_image.width - text_size[2]) // 2
        y = (original_image.height  - text_size[3] ) // 2
        # Draw the watermark text on the transparent image
        draw.text((x+width_plus, y+height_plus), watermark_text, font=font, fill=(255, 255, 255, 128))

    # Composite the original image and the watermark
    watermarked_image = Image.alpha_composite(original_image.convert("RGBA"), watermark)

    # Save the result
    watermarked_image.save(output_image_path, format="png")

# UI + Logic
image_path = PhotoImage(file="static/title_image/image_watermarking.png")
image_label = Label(window, image=image_path)
image_label.place(relx=0.5, rely=0.4, anchor=CENTER)

# Browse button to locate an image
button = Button(text="Locate📁", command=browse_file)
button.place(relx=0.2, rely=0.9, anchor=CENTER)

# Convert button to apply watermark and save the image
button = Button(text="Convert➡️", command=lambda: insert_watermark(original_img_path, OUTPUT_PATH, WATERMARK_TEXT))
button.place(relx=0.7, rely=0.9, anchor=CENTER)

# Start the main loop
mainloop()
