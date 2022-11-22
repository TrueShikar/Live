import os

from keep_alive import keep_alive

keep_alive()

os.system('ffmpeg -re -i https://ww1.shikaritv.tk/gocast.php?v=fox503 -i  "https://bold-silence-0eed.shikari.workers.dev/0:/20221108_134525.png" -filter_complex "overlay=1000:20" -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmps://rtmp-global.cloud.vimeo.com:443/live/ab51f5ea-47e7-4d0c-bcfe-b5b92594e8cf')
os.system('python3 main.py')

