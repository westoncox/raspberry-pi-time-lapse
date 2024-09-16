#!/use/bin/python3
import os
import sys
import time
import logging
from picamera2 import Picamera2

logging.basicConfig(level=logging.DEBUG)

# Set the correct USB mount path
output_directory = '/media/pi/67F7-A24D/timelapse24'
os.makedirs(output_directory, exist_ok=True)

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

# capture photos at the specified interval
start_time = time.time()
next_capture_time = time.time() + interval
while time.time() - start_time < duration:
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f'photo_{timestamp}.jpeg'
    output_file = os.path.join(output_directory, filename)
    
    logging.info(f'Attempting to save image to: {output_file}')
    
    try:
        picam2.capture_file(output_file)
        logging.info(f'Image saved: {output_file}')
    except PermissionError:
        logging.error(f'Permission denied: Unable to write to {output_file}')
    except IOError as e:
        logging.error(f"I/O error({e.errno}): {e.strerror}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    
    time.sleep(max(0, next_capture_time - time.time()))
    next_capture_time += interval

picam2.close()
logging.info("Time-lapse complete!")
