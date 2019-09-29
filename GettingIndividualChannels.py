from PIL import Image

doctor = Image.open(r"assets/Jaryan Khoshkhim.png")
red_channel, green_channel, blue_channel, alpha_channel = doctor.split()

red_channel.show()
