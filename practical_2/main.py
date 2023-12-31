import re
import argparse
import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi,noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import  text,show_message
from luma.core.legacy.font import proportional,CP437_FONT,TINY_FONT,SINCLAIR_FONT,LCD_FONT


def blinkit(n,block_orentation,rotate,msg):
    serial=spi(port=0,device=0,gpio=noop())
    device=max7219(serial,cascaded=n or 1,block_orientation=block_orientation,rotate=rotate or 0)
    show_message(device,msg,fill="white",font=proportional(LCD_FONT),scroll_delay=0.1)
    time.sleep(3)
    pass

if __name__=="__main__":
    try:
        text_display=raw_input("enter whatever you want")
        blinkit(1,0,0,text_display)
    except KeyboardInterrupt:
        pass
    finally:
        print("program exit")

