from PIL import Image

# doctor = Image.open(r"assets/Jaryan Khoshkhim.png")
# r, g, b, a = doctor.split()
# new_img = Image.merge("RGBA", (b, g, r, a))
#
# new_img.show()


ravanshenas = Image.open(r"assets/Ravanshenas.png")
chayi_nabat = Image.open(r"assets/Chayi.png")
r1, g1, b1, *_ = ravanshenas.split()
r2, g2, b2, *_ = chayi_nabat.split()

new_img = Image.merge("RGB", (r1, g1, b2))
new_img.show()
