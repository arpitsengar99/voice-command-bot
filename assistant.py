import speech_recognition as sr
import pyttsx3
from pyautogui import*

# Initialize the recognizer
r = sr.Recognizer()

# Funtion to convert text to
# speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    
    engine.say(command)
    engine.runAndWait()
    
    
# Loop infinitely for user to
# speak
print('Loading')
write('....', interval = 1)
SpeakText('Hello, how can i help you')
print('Hello, how can i help you')

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
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower().split(" ")
            print(MyText)
            if "song" in MyText:             
            # if MyText == 'play a song' or MyText == "mujhe ek gana sunna hai" :
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
                                                    
                                    
            # elif MyText == "show my channel on youtube":
            #                                         SpeakText('Opening Youtube')
            #                                         print('Opening youtube')
            #                                         keyDown('win')
            #                                         press('r')
            #                                         keyUp('win')
            #                                         write('brave')
            #                                         press('enter', interval = 3)
            #                                         write('https://www.youtube.com/channel/UCDzWo3sdRD6LnQUETpFpP4g/videos')
            #                                         press('enter')            
                                              
            # elif MyText == "play that song":
            #                                         SpeakText('Now playing After Dark x Sweater Weather from youtube')
            #                                         print('Now playing After Dark x Sweater Weather from youtube')
            #                                         keyDown('win')
            #                                         press('r')
            #                                         keyUp('win')
            #                                         write('brave')
            #                                         press('enter', interval = 3)
            #                                         write('https://youtu.be/hvL-2TF9bLY')
            #                                         press('enter')           

            elif "decrease" in MyText:
                                                    SpeakText("Decreasing the volume by 20")
                                                    print("Volume decreased by 20")
                                                    for i in range(11):
                                                        press('volumedown')

            elif "increase" in MyText:
                                                    SpeakText("Increasing the volume by 20")
                                                    print("Volume increased by 20")
                                                    for i in range(11):
                                                        press('volumeup')

            elif "mute" in MyText:
                                                    SpeakText("Volume muted")
                                                    print("Volume muted")
                                                    press('volumemute')
                                                
            elif "unmute" in MyText:
                                                    SpeakText("Volume unmuted")
                                                    print("Volume unmuted")
                                                    press('volumemute')
            
            elif "home" in MyText:                              
                                                    keyDown('win')
                                                    press('d')
                                                    keyUp('win')
            
            elif "switch" in MyText:
                                                    SpeakText("Switching tabs")
                                                    print("Tabs switched")
                                                    keyDown('alt')
                                                    press('tab')
                                                    keyUp('alt')

            elif "create" in MyText:
                                                    SpeakText("Creating a desktop")
                                                    print("Desktop created successfully")
                                                    keyDown('win')
                                                    keyDown('ctrl')
                                                    press('d')
                                                    keyUp('ctrl')
                                                    keyDown('win')
            elif "close" in MyText: 
                                                    for i in range(10):
                                                        keyDown('win')
                                                        keyDown('ctrl')
                                                        press('f4')
                                                        keyUp('ctrl')
                                                        keyDown('win')
                                                    SpeakText("Deleting all the desktops")
                                                    print("All desktops deleted successfully")
                                                    
                                                    
            elif "minimise" in MyText:
                                                    print("Window minimized")
                                                    keyDown('win')
                                                    press('down')
                                                    keyUp('win')
                                                    
            elif "close" in MyText :
                                                    print("Application closed")
                                                    keyDown('alt')
                                                    press('f4')
                                                    keyUp('alt')

            elif "left" in MyText:
                                                    print("Desktop switched to the left")
                                                    keyDown('win')
                                                    keyDown('ctrl')
                                                    press('left')
                                                    keyUp('ctrl')
                                                    keyDown('win')

            elif "right" in MyText:
                                                    print("Desktop switched to the right")
                                                    keyDown('win')
                                                    keyDown('ctrl')
                                                    press('right')
                                                    keyUp('ctrl')
                                                    keyDown('win')

            elif "shutdown" in MyText or "shut" in MyText:
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
                
            elif "reboot" in MyText:
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
            
            elif "refresh" in MyText:
                                                    keyDown('win')
                                                    press('d')
                                                    keyUp('win')
                                                    for i in range(2):
                                                        keyDown('fn')
                                                        press('f5')
                                                        keyUp('fn')
                                                    print("System refreshed")

            elif "maximum" in MyText:            
                                                    for i in range(50):
                                                        press('volumeup')
                                                    print("Volume maximised")
            elif "open" in MyText:
                                                    SpeakText('Okay what would you like to open?')
                                                    print('Okay what would you like to open?')
                                                    # print("Okay what song would you like to hear?")
                                                    audio2 = r.listen(source2)            
                                                    # Using google to recognize audio
                                                    MySong = r.recognize_google(audio2)
                                                    MySong = MySong.lower()
                                                    press("win")
                                                    write(MySong, interval = 0.1)
                                                    press("enter")
                                                   
                                                                                                      
            else:
                print("Sorry i could not understand that ")
                # SpeakText("Sorry i could not understand that")
                            
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("******")
    
