import datetime
import time
import os

daytime = -1
changed = False

while True:
	now = datetime.datetime.now()
	
	if   now.hour < 4 and time != 3:
		daytime = 3
		changed = True
	elif now.hour < 10 and time != 0:
		daytime = 0
		changed = True
	elif now.hour < 16 and time != 1:
		daytime = 1
		changed = True
	elif now.hour < 22 and time != 2:
		daytime = 2
		changed = True
	elif time != 3:
		daytime = 3
		changed = True	
	
	if changed:
		changed = False	
		os.system("gsettings set org.gnome.desktop.background picture-uri file://$HOME/.config/i3/backgrounds/vally-"+str(daytime)+".jpg")
		os.system("feh --bg-scale $HOME/.config/i3/backgrounds/vally-"+str(daytime)+".jpg")
	
	time.sleep(10)
