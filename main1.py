import os

from keep_alive import keep_alive

keep_alive()

os.system('ffmpeg -re -i https://mx.techyshikari.in/Bb24x7.m3u8 -i  "https://bold-silence-0eed.shikari.workers.dev/0:/20221108_134525.png" -filter_complex "overlay=1000:20" -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmps://rtmp-global.cloud.vimeo.com:443/live/d7cd6e68-61cf-4e75-844a-5d66972e7fc4')
os.system('python3 main.py')

