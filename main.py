from moviepy import *
import pygame
import time

badApple = VideoFileClip("badApple.mp4")
badApple = badApple.resized(width=1, height=1)
length = badApple.duration

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

mode = input(str(f"What do you want to do?\n"
          f"1. Watch\n"
          f"2. Watch Enhanced\n"
          f"3. Download\n"
                 f"4. Enhanced Download\n"
                 f"Input a number: "))

if mode == "1":
    badApple.preview()
    time.sleep(length)
    badApple.close()
elif mode == "2":
    badApple = badApple.resized(width=100, height=100)
    badApple.preview()
    time.sleep(length)
    badApple.close()
elif mode == "3":
    badApple.write_videofile("badApple1x1.mp4", fps=badApple.fps)
elif mode == "4":
    badApple = badApple.resized(width=1000, height=1000)
    badApple.write_videofile("badApple1x1enhanced.mp4", fps=badApple.fps)

