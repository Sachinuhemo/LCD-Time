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

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

# フォント
font_path = "/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf"
font = ImageFont.truetype(font_path, 15)

try:
    # 現在日時
    dt_now = datetime.datetime.now()
    while True:

        # 時間が変わったなら
        if dt_now.second != datetime.datetime.now().second:
            dt_now = datetime.datetime.now()
            if dt_now.minute == 0 and dt_now.second < 10:
                if dt_now.month == 1 and dt_now.day == 1:
                    font = ImageFont.truetype(font_path, 30)
                    text = dt_now.strftime('%Y年')

                elif dt_now.hour == 0 or dt_now.hour == 12:
                    font = ImageFont.truetype(font_path, 30)
                    week = datetime.datetime.now().weekday()
                    if week == 0:
                        text = dt_now.strftime('%m/%d 月')
                    elif week == 1:
                        text = dt_now.strftime('%m/%d 火')
                    elif week == 2:
                        text = dt_now.strftime('%m/%d 水')
                    elif week == 3:
                        text = dt_now.strftime('%m/%d 木')
                    elif week == 4:
                        text = dt_now.strftime('%m/%d 金')
                    elif week == 5:
                        text = dt_now.strftime('%m/%d 土')
                    elif week == 6:
                        text = dt_now.strftime('%m/%d 日')

                else:
                    text = dt_now.strftime('%Y年%m月%d日\n%H時%M分%S秒')
                    draw.rectangle((0, 0, width, height), outline=0, fill=1)
                    draw.text((0, 0), text, font=font, fill=0)
                    disp.image(image)
                    disp.display()
                    continue    # while文の一番最初に戻る

                draw.rectangle((0, 0, width, height), outline=0, fill=1)
                draw.text((0, 0), text, font=font, fill=0)
                disp.image(image)
                disp.display()
                time.sleep(9)
                font = ImageFont.truetype(font_path, 15)

            else:
                text = dt_now.strftime('%Y年%m月%d日\n%H時%M分%S秒')
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                draw.text((0, 0), text, font=font, fill=1)
                disp.image(image)
                disp.display()

# Ctrl + C
except KeyboardInterrupt:
        disp.clear()
        disp.display()
