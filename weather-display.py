from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from datetime import date
import textwrap
import requests
import json
from astral import LocationInfo
from suntime import Sun, SunTimeException

wgovres = requests.get("https://api.weather.gov/gridpoints/CLE/79,63/forecast")
wgovjson = json.loads(wgovres.text)
#print(wgovjson["properties"]['periods'][0])
forcasts = wgovjson["properties"]['periods']

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

temphumfontsize = 25
temphumfont = ImageFont.truetype(FredokaOne, temphumfontsize)

tempvalx = 130
tempvaly = 25
tempvalstr = str(forcasts[0]['temperature']) + "°"
draw.text((tempvalx, tempvaly), tempvalstr, inky_display.BLACK, temphumfont)

# sun rise and set
sunriseimg = Image.open("/home/pi/weather-display/wi-sunrise.png")
sunrimgx = 0
sunrimgy = 225
img.paste(sunriseimg, (sunrimgx, sunrimgy))

sunfontsize = 20
sunfont = ImageFont.truetype(FredokaOne, sunfontsize)

sunt = Sun(41.4808,-81.8003)

today_sr = sunt.get_local_sunrise_time()
today_ss = sunt.get_local_sunset_time()

sunrtimex = 55
sunrtimey = 230
sunrtimestr = today_sr.strftime('%-I:%M %p')
print(sunrtimestr)
draw.text((sunrtimex, sunrtimey), sunrtimestr, inky_display.BLACK, sunfont)

sunsetimg = Image.open("/home/pi/weather-display/wi-sunset.png")
sunsimgx = 0
sunsimgy = 262
img.paste(sunsetimg, (sunsimgx, sunsimgy))

sunstimex = 55
sunstimey = 262
sunstimestr = today_ss.strftime('%-I:%M %p')
print(sunstimestr)
draw.text((sunstimex, sunstimey), sunstimestr, inky_display.BLACK, sunfont)

# moon phase
sunsetimg = Image.open("/home/pi/weather-display/wi-moon-alt-waxing-gibbous-2.png")
moonx = 150
moony = 240
img.paste(sunsetimg, (moonx, moony))

# current detailed forcast
# if details about this long:
# "Partly sunny, with a high near 26. Northwest wind 9 to 13 mph"
# then double font? font size 20, width 20
# else if about this long (that seems about max)
# "Snow likely after 7pm. Cloudy, with a low around 27. Southeast wind 8 to 12 mph. Chance of precipitation is 70%. New snow accumulation of less than one inch possible."
# "A chance of snow before 7pm, then a chance of snow showers. Cloudy, with a low around 25. North wind 13 to 18 mph. Chance of precipitation is 50%. New snow accumulation of around one inch possible."
#then font size should stay about 13, width 35
current_detailed = forcasts[0]['detailedForecast']

curdetailfontsize = 20
curdetailfont = ImageFont.truetype(FredokaOne, curdetailfontsize)


lines = textwrap.wrap(current_detailed, width=20)
curdetailx = 0
curdetaily = 100
currentwidth, currentheight = curdetailfont.getsize(current_detailed)
for line in lines:
    draw.text((curdetailx, curdetaily), line, inky_display.BLACK, curdetailfont)
    curdetaily += currentheight


# later forcast
forcastimgx = 210
#forcastimgy = 0

forcastdaysize = 18
forcastdayfont = ImageFont.truetype(FredokaOne, forcastdaysize)
forcastdayx = 260
#forcastdayy = 0

forcastdetailsize = 13
forcastdetailfont = ImageFont.truetype(FredokaOne, forcastdetailsize)
forcastdetailx = 210
#forcastdetaily = 50

forcastdetailtempx = 260
#forcastdetailtempy = 22
#draw.text((forcastdetailtempx, forcastdetailtempy), forcastdetailtemp, inky_display.BLACK, forcastdayfont)

forcastyoffset = 75
for x in range(0, 4):
    forcastimg = Image.open("/home/pi/weather-display/wi-snow.png")
    forcastimgy = x*forcastyoffset
    img.paste(forcastimg, (forcastimgx, forcastimgy))
    forcastdaymsg = forcasts[x+1]['name']
    forcastdayy = x*forcastyoffset
    draw.text((forcastdayx, forcastdayy), forcastdaymsg, inky_display.BLACK, forcastdayfont)
    forcastdetailmsg = forcasts[x+1]['shortForecast']
    lines = textwrap.wrap(forcastdetailmsg, width=30)
    forcastdetailwidth, forcastdetailheight = forcastdetailfont.getsize(forcastdetailmsg)
    forcastdetaily = 48+(x*forcastyoffset)
    for line in lines:
        draw.text((forcastdetailx, forcastdetaily), line, inky_display.BLACK, forcastdetailfont)
        forcastdetaily += forcastdetailheight
    forcastdetailtemp = str(forcasts[x+1]['temperature'])+"°"
    forcastdetailtempy = 22 + (x*forcastyoffset)
    draw.text((forcastdetailtempx, forcastdetailtempy), forcastdetailtemp, inky_display.BLACK,forcastdayfont)


inky_display.set_image(img)
inky_display.show()

