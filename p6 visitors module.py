import RPi.GPIO as gpio
import picamera
import time
m11=17
m12=27
led=5
buz=26
button=19
HIGH=1
LOW=0
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)
gpio.setup(buz, gpio.OUT)
gpio.setup(m11, gpio.OUT)
gpio.setup(m12, gpio.OUT)
gpio.setup(button, gpio.IN)
gpio.output(led , 0)
gpio.output(buz , 0)
gpio.output(m11 , 0)
gpio.output(m12 , 0)
data=""
def capture_image():
    print("Please Wait..");
    data= time.strftime("%d_%b_%Y\%H:%M:%S")
    camera.start_preview()
    time.sleep(5)
    print (data)
    camera.capture('/home/pi/Desktop/Visitors/%s.jpg'%data)
    camera.stop_preview()
    print("Image Captured Successfully")
    time.sleep(2)
def gate():
            print("    Welcome  ")
            gpio.output(m11, 1)
            gpio.output(m12, 0)
            time.sleep(1.5)
            gpio.output(m11, 0)
            gpio.output(m12, 0)
            time.sleep(3)
            gpio.output(m11, 0)
            gpio.output(m12, 1)
            time.sleep(1.5)
            gpio.output(m11, 0)
            gpio.output(m12, 0)
            print("  Thank You  ")
            time.sleep(2)
print("Visitor Monitoring")
print("    Using RPI     ")
time.sleep(3)
camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55
time.sleep(2)
while 1:
        print(" Please Press Button")
        print("  to open the gate  ")
        gpio.output(led, 1)
        if gpio.input(button)==0:
            gpio.output(buz, 1)
            gpio.output(led, 0)
            time.sleep(0.5)
            gpio.output(buz, 0)
            capture_image()
            gate()
        time.sleep(0.5)
