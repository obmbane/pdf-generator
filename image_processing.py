from PIL import Image

# Open an image file
image = Image.open("Picture1.png")

# Resize the image
new_size = (300, 300)  # Width, height
resized_image = image.resize(new_size)

# Save the resized image
resized_image.save("resized_image1.png")








