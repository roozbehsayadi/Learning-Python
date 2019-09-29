from PIL import Image

img = Image.open(r"assets/Jaryan Khoshkhim.png")
area = (513, 44, 995, 526)
cropped_image = img.crop(area)

img.show()
cropped_image.show()
