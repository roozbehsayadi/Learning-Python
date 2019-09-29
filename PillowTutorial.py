from PIL import Image

img = Image.open("assets/Jaryan Khoshkhim.png")
print(img.size)
print(img.format)

img.show()
