from inky import InkyWHAT

inky_display = InkyWHAT("black")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne

font = ImageFont.truetype(FredokaOne, 36)

message = "hi ilona"
w, h = font.getsize(message)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), message, inky_display.BLACK, font)

weatherimg = Image.open("/home/pi/weather-display/wi-day-cloudy.png")
offset = (0,0)
img.paste(weatherimg, offset)
inky_display.set_image(img)
inky_display.show()


