#Create Basic Tkinter Gui
from tkinter import  *
from tkinter import filedialog
from PIL import  Image, ImageDraw, ImageFont

OUTPUT_PATH=r".\static\done_watermarking\image_with_watermark.png"
WATERMARK_TEXT="Official_Beast"
window = Tk()
window.minsize(width=500,height=500)
window.title("Image-Watermarking")

#input=  a image

#output=  a image with my water mark



#Add a file locator and load that image in variable
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        insert_watermark(file_path,OUTPUT_PATH,watermark_text=WATERMARK_TEXT)







#try to find a way to insert the
# watermark in Image
def insert_watermark(input_image_path,output_image_path,watermark_text,font_size=36):
    # Open the original image
    original_image = Image.open(input_image_path)

    # Create a transparent image for the watermark
    watermark = Image.new("RGBA", original_image.size, (255, 255, 255, 0))

    # Choose a font and size for the watermark
    font = ImageFont.truetype("path/to/your/font.ttf", font_size)

    # Create a drawing context for the watermark
    draw = ImageDraw.Draw(watermark)

    # Calculate the size of the watermark text
    text_size = draw.textbbox((0, 0), watermark_text, font)

    # Calculate the position to center the watermark on the image
    x = (original_image.width - text_size[2]) // 2
    y = (original_image.height - text_size[3]) // 2

    # Draw the watermark text on the transparent image
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    # Composite the original image and the watermark
    watermarked_image = Image.alpha_composite(original_image.convert("RGBA"), watermark)

    # Save the result
    watermarked_image.save(output_image_path,format="png")



#after that try to find if u can  5






#*************UI**************

image_path= PhotoImage(file="static/title_image/image_watermarking.png")
image_label= Label(window,image=image_path)
image_label.place(relx=0.5,rely=0.4,anchor= CENTER)



button=Button(text="Locate📁",command=browse_file)
button.place(relx=0.2,rely=0.7, anchor=CENTER)


button=Button(text="Convert➡️")
button.place(relx=0.7,rely=0.7, anchor=CENTER)


# **********Logic*********





mainloop()