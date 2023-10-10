from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera=PiCamera()
camera.resolution=(1280,720)
camera.framerate=60
rawCapture=PiRGBArray(camera,size=(3840,720))
print("<warming uo>")

camera.start_preview()
time.sleep(5)
camera.capture("give the path")
camera.stop_preview()

camera.start_preview()
for i in range(5):
    time.sleep(5)
    camera.capture("path/image%s.jpg"%i)

camera.stop_preview()
