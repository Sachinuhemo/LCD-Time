import time
import datetime
from PIL import Image, ImageDraw, ImageFont
import Adafruit_SSD1306

# Initialization of OLED display
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None, i2c_address=0x3C)
disp.begin()

# turn off the screen
disp.clear()
disp.display()

# image
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

# font
font_path = "/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf"
font = ImageFont.truetype(font_path, 15)

try:
    now = datetime.datetime.now()
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    while True:

        if now.second != datetime.datetime.now().second:
            now = datetime.datetime.now()
            if now.minute == 0 and now.second == 0:
                if now.month == 1 and now.day == 1:
                    font = ImageFont.truetype(font_path, 30)
                    text = now.strftime('%Y')
                    draw.rectangle((0, 0, width, height), outline=0, fill=1)
                    draw.text((0, 0), text, font=font, fill=0)
                    disp.image(image)
                    disp.display()
                    text = ('01/01')
                    time.sleep(5)
                    draw.rectangle((0, 0, width, height), outline=0, fill=1)
                    draw.text((0, 0), text, font=font, fill=0)
                    disp.image(image)
                    disp.display()
                    font = ImageFont.truetype(font_path, 15)
                    time.sleep(5)

                elif now.hour == 0 or now.hour == 12:
                    font = ImageFont.truetype(font_path, 30)
                    text = now.strftime('%m/%d')
                    draw.rectangle((0, 0, width, height), outline=0, fill=1)
                    draw.text((0, 0), text, font=font, fill=0)
                    disp.image(image)
                    disp.display()
                    font = ImageFont.truetype(font_path, 15)
                    time.sleep(10)

                else:
                    weekday_str = weekdays[now.weekday()]
                    text = now.strftime('%Y/%m/%d') + f' {weekday_str}\n' + now.strftime('%H:%M:%S')
                    draw.rectangle((0, 0, width, height), outline=0, fill=1)
                    draw.text((0, 0), text, font=font, fill=0)
                    disp.image(image)
                    disp.display()
                    while now.second <= 9:
                        if now.second != datetime.datetime.now().second:
                            now = datetime.datetime.now()
                            weekday_str = weekdays[now.weekday()]
                            text = now.strftime('%Y/%m/%d') + f' {weekday_str}\n' + now.strftime('%H:%M:%S')
                            draw.rectangle((0, 0, width, height), outline=0, fill=1)
                            draw.text((0, 0), text, font=font, fill=0)
                            disp.image(image)
                            disp.display()
                            draw.rectangle((0, 0, width, height), outline=0, fill=1)
                            draw.text((0, 0), text, font=font, fill=0)
                            disp.image(image)
                            disp.display()

            else:
                weekday_str = weekdays[now.weekday()]
                text = now.strftime('%Y/%m/%d') + f' {weekday_str}\n' + now.strftime('%H:%M:%S')
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                draw.text((0, 0), text, font=font, fill=1)
                disp.image(image)
                disp.display()

# Ctrl + C
except KeyboardInterrupt:
        disp.clear()
        disp.display()
