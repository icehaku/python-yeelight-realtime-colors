import image
import pyscreenshot as ImageGrab
import time

from colorthief import ColorThief
from colr import color
from yeelight import Bulb

# SETUP PRINT SCREEN
# Quanto menor a foto, mais rapido. TODO: Testar benchmarks depois...
# Coordenadas: (x1, y1, x2, y2)
MONITOR1 = (0, 0, 1920, 1080)
MONITOR2 = (-1920, 0, 0, 1080)
MONITOR2_SMALLXX = (-1040, 400, -880, 600)
MONITOR2_SMALLX = (-1240, 270, -680, 810)
MONITOR2_SMALL = (-1440, 270, -480, 810)
MONITOR2_MEDIUM = (-1640, 270, -480, 810) # todo

SCREENSHOT_REGION = MONITOR2_SMALLX
# UPDATE_FREQUENCY = 3


def get_color(region):
	# Printando a tela e salvando
    my_image = ImageGrab.grab(bbox=SCREENSHOT_REGION, backend='mss', childprocess=False)
    my_image.save('screenshot.png')

    # Usando o pacote color_thief pra pegar a cor predominante
    color_thief = ColorThief('screenshot.png')
    main_color = color_thief.get_color(quality=1)
    
    return main_color


# def my_path
	# import os
	# import sys
	# print(os.path.dirname(sys.executable))

# def pywin32_info
	# https://github.com/mhammond/pywin32
	# https://github.com/mhammond/pywin32/releases

while True:
	# print("omegalul")

	# from yeelight import discover_bulbs
	# print("discovering bulbs")
	# discover_bulbs()

	# input('discovered?')

	print("Getting color...")
	my_color = get_color(SCREENSHOT_REGION)
	color_string = str(my_color)

	print("Got color: "+color_string)
	print(color('               ', fore=my_color, back=my_color))
	print(color('               ', fore=my_color, back=my_color))
	print(color('               ', fore=my_color, back=my_color))
	print(color('               ', fore=my_color, back=my_color))
	print(color('               ', fore=my_color, back=my_color))

	print("Changing Bulb color...")

	bulb = Bulb("192.168.15.27")	
	bulb.set_rgb(my_color[0],my_color[1],my_color[2])
	# bulb.set_rgb(255,0,0) # red
	# bulb.set_rgb(0,0,255) # blue
	# print("Waiting "+str(UPDATE_FREQUENCY)+" seconds to get color again")
	# time.sleep(UPDATE_FREQUENCY)
