from time import sleep
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()

sleep(2)
camera.capture('/home/pi/Pictures/newImage.jpg')
camera.stop_preview()

from time import sleep
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
