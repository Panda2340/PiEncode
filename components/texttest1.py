from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

inky_display = InkyPHAT('red')

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("Arial.ttf", 22)

text = "PiEncode"

w,h = draw.textsize(text, font)
x = (inky_display.WIDTH - w) / 2
y = (inky_display.HEIGHT - h) / 2

draw.text((x, y), text, inky_display.BLACK, font=font)

inky_display.set_image(img)
inky_display.show()
