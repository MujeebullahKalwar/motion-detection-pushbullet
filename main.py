from gpiozero import MotionSensor
from gpiozero import LED
from picamera import PiCamera  
import time
from time import sleep

led = LED(17)
pir = MotionSensor(4)
camera = PiCamera()
camera.rotation = 180

while True:
   pir.wait_for_motion()
   print("Motion detected!")
   camera.start_preview()
   led.on()
   filename = "/home/pi/Desktop/" + (time.strftime("%y%b%d_%H:%M:%S")) + ".h264"
   camera.start_recording(filename)
   pir.wait_for_no_motion()
   print("Motion Stopped!")
   camera.stop_recording()
   led.off()
   camera.stop_preview()
