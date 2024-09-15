from picamera2 import Picamera2
import os
import time
import logging

logging.basicConfig(level=logging.DEBUG)

picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (2028, 1080)})
picam2.configure(config)

picam2.rotation = 0
picam2.exposure_mode = 'auto'
picam2.awb_mode = 'auto'

picam2.start()
time.sleep(2)

# timelapse settings
interval = 5  # seconds between photos
duration = 15  # timelapse duration in seconds 3600 = 1 hour
output_directory = "/mnt/usb/timelapse24"
os.makedirs(output_directory, exist_ok=True)

# capture photos at the specified interval
start_time = time.time()
while time.time() - start_time < duration:
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"photo_{timestamp}.jpeg"
    output_file = os.path.join(output_directory, filename)
    
    print(f"Attempting to save image to: {output_file}")
    
    try:
        picam2.capture_file(output_file)
        print(f"Image saved: {output_file}")
    except PermissionError:
        print(f"Permission denied: Unable to write to {output_file}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    time.sleep(interval)

picam2.close()
print("Time-lapse complete!")