from PIL import Image

doctor = Image.open("assets/Jaryan Khoshkhim.png")
mard = Image.open("assets/Mard.png")

area = (20, 100, 644, 768)
doctor.paste(mard, area)

doctor.show()
