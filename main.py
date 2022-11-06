import os

from keep_alive import keep_alive

keep_alive()

os.system('ffmpeg -re -i https://da.gd/grBQl -i  "https://te.legra.ph/file/1f9f9a7e49978b17da41e.jpg" -filter_complex "overlay=10:10" -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://ovsu.mycdn.me/input/720360974_720360974_43_pgi2q3qkha')
os.system('python3 main1.py')

