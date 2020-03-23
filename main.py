import serial
import time


def open_port(port):
    ser = serial.Serial(port,9600)
    while(ser.readline() != b'ready\r\n'):
        pass
    print('opened port')
    return(ser)

def set_brightness(brightness, ser):
    ser.write(str(brightness).encode('utf-8'))

def take_photo(ISO, blah):
    print("Taking a photo with iso" + str(ISO) + "blah" + blah)


take_photo(200,'asdf')


""" ser = open_port('/dev/ttyUSB0')

set_brightness(50, ser)

time.sleep(1)

set_brightness(100, ser)

time.sleep(1)

set_brightness(40, ser) """



# camera settings that show up: analog_gain, awb_blue_gain, awb_red_gain, digital_gain, exposure, focus_position
# camera notes: AWB_MODES (0:9, random shit
# DRC_STRENGTHS: 0:3, off to high
# EXPOSURE_MODES: 0:12, random shit 
# IMAGE_EFFECTS: 0:21, random shit
# METER_MODES: 0:3, average, backlit, matrix, spot
# analog_gain: Fraction
# awb_gains: 2 fractions
# digital_gain: fraction
# drc_strength: off, low, medium, high
# exposure_compensation, -25:25
# exposure_speed: microseconds, read only, set shutter_speed instead
# image_denoise: bool
# iso: 100,200,320,400,500,640,800
# 