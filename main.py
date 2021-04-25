#### HELPER ####
# install these asll libs by using pip command (pip install pushbullet.py)
# put your push bullet access token in api_key variable

import time
from gpiozero import MotionSensor
from gpiozero import LED
from picamera import PiCamera
from pushbullet import Pushbullet
from time import sleep

api_key = 'o.153YMqXs2q4BiH2SyDaA0egWRuoECXcf'
led = LED(17)
pir = MotionSensor(4)
camera = PiCamera()
camera.rotation = 180
pb = Pushbullet(api_key)

while True:
   try:
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
      push = pb.push_note("Motion detected", "Please see tht attached file")
      with open(filename, "rb") as file_data:
         file_data = pb.upload_file(file_data, "recording.h264")
      push = pb.push_file(**file_data)
      print('Recording Sent')
   except Exception as e:
      print('ERROR:', e)
   