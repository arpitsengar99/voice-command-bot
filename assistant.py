import speech_recognition as sr
import pyttsx3
from pyautogui import*
from playsound import playsound
from tkinter import messagebox
import random as rn

FAILSAFE = False
engine = pyttsx3.init()
r = sr.Recognizer()
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait() 

# swirlTheNumbers = """"
playsound("C:/Users/asus/Desktop/project1/audio/yccms.mp3")
print("Listening....")

"""
Commands list:
1. Mute
2. Unmute
3. Volume Increase
4. Volume Decrease
5. Sign off
6. Home Screen
7. Switch tabs
8. Create Desktop
9. Close Desktop
10. Minimise
11. Left screen
12. Right screen
"""

while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower().split(" ")
            print(MyText)
            match MyText:
                case "song":            
                                                    SpeakText('Okay what song would you like to hear?')
                                                    print("Okay what song would you like to hear?")
                                                    audio2 = r.listen(source2)            
                                                    # Using google to recognize audio
                                                    MySong = r.recognize_google(audio2)
                                                    MySong = MySong.lower()
                                                    keyDown('win')
                                                    press('r')
                                                    keyUp('win')
                                                    write('brave')
                                                    press('enter', interval = 3)
                                                    write('https://www.youtube.com', interval = 0.1)
                                                    press('enter', interval = 4)
                                                    press('/')                                                    
                                                    x = MySong + ' song'
                                                    write(x, interval = 0.1)
                                                    press('enter', interval = 3)
                                                    click(x=600, y= 380, button = 'left')         

                case "decrease":
                                                    SpeakText("Decreasing the volume by 20")
                                                    print("Volume decreased by 20")
                                                    for i in range(11):
                                                        press('volumedown')

                case "increase":
                                                    SpeakText("Increasing the volume by 20")
                                                    print("Volume increased by 20")
                                                    for i in range(11):
                                                        press('volumeup')

                case "mute":
                                                    SpeakText("Volume muted")
                                                    print("Volume muted")
                                                    press('volumemute')
                                                
                case "unmute":
                                                    SpeakText("Volume unmuted")
                                                    print("Volume unmuted")
                                                    press('volumemute')
            
                case "home":                              
                                                    keyDown('win')
                                                    press('d')
                                                    keyUp('win')
            
                case "switch":
                                                    SpeakText("Switching tabs")
                                                    print("Tabs switched")
                                                    keyDown('alt')
                                                    press('tab')
                                                    keyUp('alt')

                case "create":
                                                    SpeakText("Creating a desktop")
                                                    print("Desktop created successfully")
                                                    keyDown('win')
                                                    keyDown('ctrl')
                                                    press('d')
                                                    keyUp('ctrl')
                                                    keyDown('win')
                case "close": 
                                                    for i in range(10):
                                                        keyDown('win')
                                                        keyDown('ctrl')
                                                        press('f4')
                                                        keyUp('ctrl')
                                                        keyDown('win')
                                                    SpeakText("Deleting all the desktops")
                                                    print("All desktops deleted successfully")
                                                    
                                                    
                case "minimize":
                                                    print("Window minimized")
                                                    keyDown('win')
                                                    press('down')
                                                    keyUp('win')
                                                    
                case "close":
                                                    print("Application closed")
                                                    keyDown('alt')
                                                    press('f4')
                                                    keyUp('alt')

                case "left":
                                                    print("Desktop switched to the left")
                                                    keyDown('win')
                                                    keyDown('ctrl')
                                                    press('left')
                                                    keyUp('ctrl')
                                                    keyDown('win')

                case "right":
                                                    print("Desktop switched to the right")
                                                    keyDown('win')
                                                    keyDown('ctrl')
                                                    press('right')
                                                    keyUp('ctrl')
                                                    keyDown('win')

                case "shutdown":
                                                    SpeakText("shutting down in")
                                                    SpeakText("5")
                                                    write('.', interval = 0.15)
                                                    SpeakText("4")
                                                    write('.', interval = 0.15)
                                                    SpeakText("3")
                                                    write('.', interval = 0.15)
                                                    SpeakText("2")
                                                    write('.', interval = 0.15)
                                                    SpeakText("1")
                                                    keyDown('win')
                                                    press('d')
                                                    keyUp('win')
                                                    keyDown('alt')
                                                    press('f4')
                                                    keyUp('alt')
                                                    press('enter')
                
                case "reboot":
                                                    SpeakText("rebooting in")
                                                    SpeakText("5")
                                                    write('.', interval = 0.25)
                                                    SpeakText("4")
                                                    write('.', interval = 0.25)
                                                    SpeakText("3")
                                                    write('.', interval = 0.25)
                                                    SpeakText("2")
                                                    write('.', interval = 0.25)
                                                    SpeakText("1")
                                                    keyDown('win')
                                                    press('d')
                                                    keyUp('win')
                                                    keyDown('alt')
                                                    press('f4')
                                                    keyUp('alt')
                                                    press('down')
                                                    press('enter')                               
            
                case "refresh":
                                                    keyDown('win')
                                                    press('d')
                                                    keyUp('win')
                                                    for i in range(2):
                                                        keyDown('fn')
                                                        press('f5')
                                                        keyUp('fn')
                                                    print("System refreshed")

                case "maximum":            
                                                    for i in range(50):
                                                        press('volumeup')
                                                    print("Volume maximised")
                
                case "open":
                                                    SpeakText('Okay is it an app?')
                                                    audio2 = r.listen(source2)
                                                    MySong = r.recognize_google(audio2)
                                                    MySong = MySong.lower()
                                                    if MySong == "yes":
                                                        press("win")
                                                        link = "whatsapp"
                                                        write(link, interval = 0.1)
                                                        press("enter")  
                                                    elif MySong == "no":
                                                        press("win")
                                                        link = "www."+MySong+".com"
                                                        write(link, interval = 0.1)
                                                        press("enter")
                                                    else:
                                                        print("error")

            
                case "test":
                                                    swirlTheNumbers = "turip.mp3"
                                                    playsound(swirlTheNumbers)
                                                    engine.runAndWait()
            
                case "number":
                                                    num = rn.randint(1,10)
                                                    swirlTheNumbers = "stn.wav"
                                                    playsound(swirlTheNumbers)
                                                    engine.say(num)
                                                    engine.runAndWait()
                                                    messagebox.showinfo("Today's number is ", num)
            
                case "piece":
                                                    swirlTheNumbers = "stn.wav"
                                                    playsound(swirlTheNumbers)
                                                    engine.say(num)
                                                    engine.runAndWait()
                                                    messagebox.showinfo("Today's number is ", num)
                                                                                                
                case _:
                    print("Sorry i could not understand that ")
                                 
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("******")
        