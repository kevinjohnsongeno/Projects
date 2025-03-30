import time
import datetime
import pygame
pygame.mixer.init()
def alarm(alarm_time):
        print(f"Alarm set for {alarm_time}")
        alarm_music="second-hand-149907.mp3"
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            if(current_time==alarm_time):
                sound_play(alarm_music)
                user_input()
                break
            time.sleep(1)
def sound_play(alarm_music):
    print("TIME IS UP!!")
    pygame.mixer.music.load(alarm_music)
    pygame.mixer.music.play(loops=-1)
def user_input():
    input(("PRESS ENTER TO STOP THE ALARM!!"))
    pygame.mixer.music.stop()
if __name__=="__main__":
    alarm_time=input("Enter the alarm time(HH:MM:SS):")
    alarm(alarm_time)