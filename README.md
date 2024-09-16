# raspberry-pi-time-lapse
 Time lapse via HQ camera module, running on raspberry pi 2 model b. Intend to save photos directly to usb flash.
NOTICE: timelapseV9.py does not work, but timelapseV10.py does. The main difference between the two is that I had the incorrect path for saving images.

For the script to work on other hardware, the user will most likely have to automate USB Mount at Boot (Add it to the /etc/fstab file).

To automate USB Mount at Boot:
1. Edit the fstab file:
sudo nano /etc/fstab
2. Add the following line, but adjust /dev/sda1 and the mount point* as necessary:
/dev/sda1 /mnt/usb vfat defaults 0 0
Save & exit.

*To determine the filesystem path as well as the drive mount point, type the following into terminal:
df -h