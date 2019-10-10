from PIL import Image
from PIL import ImageFilter

img = Image.open("assets/Ravanshenas.png")

sharp_img = Image.open("assets/SharpImage.png")
sharp_img = sharp_img.convert("RGB")
blur = sharp_img.filter(ImageFilter.BLUR)
detail = sharp_img.filter(ImageFilter.DETAIL)
edges = sharp_img.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()

# black_white = img.convert("L")
# black_white.show()
