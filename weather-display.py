from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from datetime import date
import textwrap

inky_display = InkyWHAT("black")
inky_display.set_border(inky_display.WHITE)
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

# current date header
currentdatesize = 18
currentdatefont = ImageFont.truetype(FredokaOne, currentdatesize)
curdatemsg = date.today().strftime('%A, %B %d')
currentdatex = 0
currentdatey = 0
draw.text((currentdatex, currentdatey), curdatemsg, inky_display.BLACK, currentdatefont)

# current weather image
currentweatherimg = Image.open("/home/pi/weather-display/wi-day-cloudy.png")
curwimgx = 0
curwimgy = 20
img.paste(currentweatherimg, (curwimgx, curwimgy))

# current temp and humidity
thermimg = Image.open("/home/pi/weather-display/wi-thermometer.png")
thermimgx = 95
thermimgy = 20
img.paste(thermimg, (thermimgx, thermimgy))

humidimg = Image.open("/home/pi/weather-display/wi-humidity.png")
humimgx = 95
humimgy = 50
img.paste(humidimg, (humimgx, humimgy))


temphumfontsize = 25
temphumfont = ImageFont.truetype(FredokaOne, temphumfontsize)

tempvalx = 130
tempvaly = 25
tempvalstr = "37°"
draw.text((tempvalx, tempvaly), tempvalstr, inky_display.BLACK, temphumfont)

humvalx = 130
humvaly = 55
humvalstr = "72%"
draw.text((humvalx, humvaly), humvalstr, inky_display.BLACK, temphumfont)

# sun rise and set
sunriseimg = Image.open("/home/pi/weather-display/wi-sunrise.png")
sunrimgx = 0
sunrimgy = 225
img.paste(sunriseimg, (sunrimgx, sunrimgy))

sunfontsize = 20
sunfont = ImageFont.truetype(FredokaOne, sunfontsize)

sunrtimex = 55
sunrtimey = 230
sunrtimestr = "8:08 AM"
draw.text((sunrtimex, sunrtimey), sunrtimestr, inky_display.BLACK, sunfont)

sunsetimg = Image.open("/home/pi/weather-display/wi-sunset.png")
sunsimgx = 0
sunsimgy = 262
img.paste(sunsetimg, (sunsimgx, sunsimgy))

sunstimex = 55
sunstimey = 262
sunstimestr = "4:37 PM"
draw.text((sunstimex, sunstimey), sunstimestr, inky_display.BLACK, sunfont)

# moon phase
sunsetimg = Image.open("/home/pi/weather-display/wi-moon-alt-waxing-gibbous-2.png")
moonx = 150
moony = 240
img.paste(sunsetimg, (moonx, moony))

# current detailed forcast
current_detailed = "A chance of snow showers before noon. Mostly cloudy, with a high near 23. Northwest wind around 14 mph. Chance of precipitation is 50%. New snow accumulation of less than one inch possible."

curdetailfontsize = 13
curdetailfont = ImageFont.truetype(FredokaOne, curdetailfontsize)


lines = textwrap.wrap(current_detailed, width=35)
curdetailx = 0
curdetaily = 100
currentwidth, currentheight = curdetailfont.getsize(current_detailed)
for line in lines:
    draw.text((curdetailx, curdetaily), line, inky_display.BLACK, curdetailfont)
    curdetaily += currentheight


# later forcast
forcastimg = Image.open("/home/pi/weather-display/wi-snow.png")
forcastimgx = 210
forcastimgy = 0
img.paste(forcastimg, (forcastimgx, forcastimgy))

forcastdaysize = 18
forcastdayfont = ImageFont.truetype(FredokaOne, forcastdaysize)
forcastdaymsg = "Tonight"
forcastdayx = 260
forcastdayy = 0
draw.text((forcastdayx, forcastdayy), forcastdaymsg, inky_display.BLACK, forcastdayfont)

forcastdetailsize = 13
forcastdetailfont = ImageFont.truetype(FredokaOne, forcastdetailsize)
forcastdetailmsg = "Mostly Cloudy then Slight Chance Snow Showers"
forcastdetailx = 210
forcastdetaily = 50

lines = textwrap.wrap(forcastdetailmsg, width=30)
forcastdetailwidth, forcastdetailheight = forcastdetailfont.getsize(forcastdetailmsg)
for line in lines:
    draw.text((forcastdetailx, forcastdetaily), line, inky_display.BLACK, forcastdetailfont)
    forcastdetaily += forcastdetailheight






inky_display.set_image(img)
inky_display.show()

