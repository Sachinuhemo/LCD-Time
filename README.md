![GitHub License](https://img.shields.io/github/license/Sachinuhemo/LCD-Time)
![](https://img.shields.io/github/repo-size/Sachinuhemo/LCD-Time)

[Japanese readme](https://github.com/Sachinuhemo/LCD-Time/blob/main/README-ja.md)

This is a Python program that uses a Raspberry pi to display the current date and time on an I2C LCD.
## Preparation
・Raspberry pi 3<br>
・[LCD](https://amzn.asia/d/0ixCi5Gz)<br>
・breadboard

Enable I2C communication.

## Install
```

pip install Pillow

```

## Connection
Connect GPIO2 to SDA on the LCD and GPIO3 to SCL.
Use the `i2cdetect` command to check if they are connected.
```
pi@raspberrypi:~ $ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```
It is connected because it shows 3c. If it is not connected, this is what happens.
```
pi@raspberrypi:~ $ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```
## Run
```python3
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
    weekdays = ['Mon', 'Thu', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
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
```
```

sudo pyhon3 time.py

```
<img src="https://github.com/user-attachments/assets/f5eec34b-2086-462e-b6ec-8ebdcab5a1ce" width="500">
<img src="https://github.com/user-attachments/assets/12c2d48f-52a5-4d66-a006-530bd4479081" width="500">

It is displayed like this.

<img src="https://github.com/user-attachments/assets/37543157-dff6-4f9e-9142-294c9d090206" width="500">

Japanese version.

## Websites we referred to
・[ラズパイを使って、OLED表示デバイスに文字列や画像を表示するよ](https://zenn.dev/kotaproj/articles/6f08ea43cd4dda8e0d2f)
