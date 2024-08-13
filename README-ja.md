![GitHub License](https://img.shields.io/github/license/Sachinuhemo/LCD-Time)
![](https://img.shields.io/github/repo-size/Sachinuhemo/LCD-Time)


Raspberry piを使って、現在の日時をI2C液晶に表示させるPythonのプログラムです。
## 用意したもの
・Raspberry pi 3<br>
・[I2Cディスプレイ](https://amzn.asia/d/0ixCi5Gz)<br>
・ブレッドボード

I2C通信を有効にすること。

## インストール
```

pip install Pillow

```

## 接続
GPIO2にLCDにあるSDAと接続し、GPIO3にSCLと接続する。
`i2cdetect`コマンドで、接続されているかを確認する。
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
3cと出ているので接続されている。接続されていないとこうなります。
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
## 実行
```python3
import time
import datetime
from PIL import Image, ImageDraw, ImageFont
import Adafruit_SSD1306

# OLEDディスプレイの初期化
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None, i2c_address=0x3C)
disp.begin()

# 画面を消す
disp.clear()
disp.display()

# 画像
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

# フォント
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
                    weekday_str = weekdays[now.weekday()]
                    text = (f'{weekday_str}, 01/01')
                    time.sleep(5)
                    draw.rectangle((0, 0, width, height), outline=0, fill=1)
                    draw.text((0, 0), text, font=font, fill=0)
                    disp.image(image)
                    disp.display()
                    font = ImageFont.truetype(font_path, 15)
                    time.sleep(5)

                elif now.hour == 0 or now.hour == 12:
                    font = ImageFont.truetype(font_path, 30)
                    weekday_str = weekdays[now.weekday()]
                    text = now.strftime(f'{weekday_str}, %m/%d/')
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
これを実行します。
```

sudo pyhon3 time.py

```
<img src="https://github.com/user-attachments/assets/f5eec34b-2086-462e-b6ec-8ebdcab5a1ce" width="500">
<img src="https://github.com/user-attachments/assets/12c2d48f-52a5-4d66-a006-530bd4479081" width="500">

このように表示されます。

<img src="https://github.com/user-attachments/assets/37543157-dff6-4f9e-9142-294c9d090206" width="500">

日本語バージョンです。

## 参考にさせていただいたサイト
・[ラズパイを使って、OLED表示デバイスに文字列や画像を表示するよ](https://zenn.dev/kotaproj/articles/6f08ea43cd4dda8e0d2f)
