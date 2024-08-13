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
    weekdays = ['月', '火', '水', '木', '金', '土', '日']
    while True:

        # 時間が変わったなら
        if now.second != datetime.datetime.now().second:
            now = datetime.datetime.now()
            if now.minute == 0 and now.second == 0:
                if now.month == 1 and now.day == 1:
                    font = ImageFont.truetype(font_path, 30)
                    text = now.strftime('%Y年')
                    draw.rectangle((0, 0, width, height), outline=0, fill=1)
                    draw.text((0, 0), text, font=font, fill=0)
                    disp.image(image)
                    disp.display()
                    weekday_str = weekdays[now.weekday()]
                    text = (f'01月01日 {weekday_str}')
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
                    text = now.strftime(f'%m月%d日 {weekday_str}')
                    draw.rectangle((0, 0, width, height), outline=0, fill=1)
                    draw.text((0, 0), text, font=font, fill=0)
                    disp.image(image)
                    disp.display()
                    font = ImageFont.truetype(font_path, 15)
                    time.sleep(10)

                else:
                    text = now.strftime('%Y年%m月%d日\n%H時%M分%S秒')
                    draw.rectangle((0, 0, width, height), outline=0, fill=1)
                    draw.text((0, 0), text, font=font, fill=0)
                    disp.image(image)
                    disp.display()
                    while now.second <= 9:
                        if now.second != datetime.datetime.now().second:
                            now = datetime.datetime.now()
                            text = now.strftime('%Y年%m月%d日\n%H時%M分%S秒')
                            draw.rectangle((0, 0, width, height), outline=0, fill=1)
                            draw.text((0, 0), text, font=font, fill=0)
                            disp.image(image)
                            disp.display()
                            draw.rectangle((0, 0, width, height), outline=0, fill=1)
                            draw.text((0, 0), text, font=font, fill=0)
                            disp.image(image)
                            disp.display()

            else:
                text = now.strftime('%Y年%m月%d日\n%H時%M分%S秒')
                draw.rectangle((0, 0, width, height), outline=0, fill=0)
                draw.text((0, 0), text, font=font, fill=1)
                disp.image(image)
                disp.display()

# Ctrl + C
except KeyboardInterrupt:
        disp.clear()
        disp.display()
