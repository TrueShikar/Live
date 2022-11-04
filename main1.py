import os

from keep_alive import keep_alive

keep_alive()

os.system('ffmpeg -re -i https://ww1.shikaritv.tk/stsp1hin.php -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://ovsu.mycdn.me/input/720360974_720360974_43_pgi2q3qkha')
os.system('python3 main.py')

