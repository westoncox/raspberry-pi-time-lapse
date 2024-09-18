from picamera2 import Picamera2
import os
import time

picam2 = Picamera2()
config = picam2.create_preview_configuration()
picam2.configure(config)

#picam2.resolution = (4056, 3040)
picam2.width = (4056)
picam2.height = (3040)
picam2.rawfull = 1
picam2.rotation = 0
picam2.zoom = (0.0, 0.0, 0.0, 0.0)
picam2.exposure_mode = 'auto'
picam2.awb_mode = 'auto'

picam2.start()

time.sleep(2)

#timelapse settings
interval = 600 #seconds between photos
duration = 4320000 #timelapse duration in seconds 3600 = 1 hour
output_directory = "/mnt/hd1/timelapse2024-rp24"

os.makedirs(output_directory, exist_ok=True)

#capture photos at the specified interval
start_time = time.time()
while time.time() - start_time < duration:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    output_file = os.path.join(output_directory, f"photo_{timestamp}.jpeg")
    
    #capture a photo
    picam2.capture_file(output_file, format='jpeg')

    time.sleep(interval)
picam2.close()
print("Time-lapse complete!")