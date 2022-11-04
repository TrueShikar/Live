import os

from keep_alive import keep_alive

keep_alive()

os.system('ffmpeg -re -i https://bit.ly/3kq9SCE -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://origin.playdj.tv/live/3cc0df3e-388d-4b5b-8816-1fa22ecf4bbb')
os.system('python3 main.py')

