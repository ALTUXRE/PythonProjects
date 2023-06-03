import datetime
from playsound import playsound
alarmHour = int(input("Enter Hour: "))
alarmMin = int(input("Enter Minutes: "))
alarmAM = input("am / pm: ")

if alarmAM=="pm":
    alarmHour+=12

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print ("Ringing...")
        playsound("C:\\Users\\ariha\\Downloads\\Sigma Male - Polozhenie Zedline Remix.mp3")
        break
