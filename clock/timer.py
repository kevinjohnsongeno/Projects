import time
import string
import pygame
print("WELCOME TO TIMER!!")
sound="second-hand-149907.mp3"
pygame.mixer.init()


def timer(time_s):
    for i in range(time_s, 0, -1):
        seconds = i % 60
        minutes = (i // 60) % 60
        hours = (i // 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("TIME IS UP!!")
    sound_play(sound)
    user_input()
def sound_play(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=-1)
def user_input():
    input("PRESS ENTER KEY TO STOP TO PLAYING!!")
    pygame.mixer.music.stop()

while True:

        try:
            time_s=int(input("How long would you like to set the timer for(in seconds):"))
            timer(time_s)
        except ValueError:
            print("Please enter a valid value:")

        choice = input("Would you like to continue(y/n):").strip()
        if choice.lower() == "y":
            continue
        else:
            print("THANK YOU")
            break


