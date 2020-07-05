from guizero import App, PushButton, Text, Window
from time import sleep
import time
import datetime
import sys, os
import subprocess

def clear():
    show_busy()
    os.system("rm -v /home/pi/Downloads/*")
    hide_busy()
    
def show_busy():
    busy.show()
    print("busy now")
    
def hide_busy():
    busy.hide()
    print("no longer busy")
    
def fullscreen():
    
    app.tk.attributes("-fullscreen", True)

def notfullscreen():
    
    app.tk.attributes("-fullscreen", False)

# Generate timestamp string generating name for photos
def timestamp():
    tstring = datetime.datetime.now()
    #print("Filename generated ...")
    return tstring.strftime("%Y%m%d_%H%M%S")

global capture_number
capture_number = timestamp()
video_capture_number = timestamp()

def burst():

    show_busy()
    capture_number = timestamp()
    print("Raspistill starts")
    os.system("raspistill  -t 10000 -tl 0 --thumb none -n -bm -o /home/pi/Downloads/BR" +str(capture_number) + "%04d.jpg")
    print("Raspistill done")
    hide_busy()
    
def split_hd_30m():
    
    show_busy()
    capture_number = timestamp()
    print("Raspivid starts")
    os.system("raspivid -f -t 1800000 -sg 300000  -o /home/pi/Downloads/" +str(capture_number) + "vid%04d.h264")
    print("done")
    hide_busy()
    
#def split_slo_1h():

#def long_exp():
   
def lapse():
    
    show_busy()
    capture_number = timestamp()
    print("Raspistill timelapse starts")
    os.system("raspistill  -t 3600000 -tl 60000 --thumb none -n -bm -o /home/pi/Downloads/TL" +str(capture_number) + "%04d.jpg")
    print("Raspistill timelapse done")
    hide_busy()

def long_preview():
    show_busy()
    print("30 second preview")
    os.system("raspistill -f -t 30000")
    hide_busy()

def capture_image():
    
    show_busy()
    capture_number = timestamp()
    print("Raspistill starts")
    os.system("raspistill -f -o /home/pi/Downloads/" +str(capture_number) + "cam.jpg")
    print("Raspistill done")
    hide_busy()

def video_capture():
    
    show_busy()
    capture_number = timestamp()
    print("Raspivid starts")
    os.system("raspivid -f -t 30000 -o /home/pi/Downloads/" +str(capture_number) + "vid.h264")
    print("done")
    hide_busy()

def upload():
    
    show_busy()
    subprocess.Popen(["python3", "/home/pi/TouchCam/dropit.py", "--yes"])
    hide_busy()
    
    
app = App(layout="grid", title="Camera Controls", bg="black", width=800, height=480)
space0 = PushButton(app, grid=[0,0], width=50, height=50, image="/home/pi/TouchCam/icon/100black.png", command=notfullscreen)


button = PushButton(app, grid=[1,1], width=150, height=150, image="/home/pi/TouchCam/icon/prev.png", command=long_preview)
text1 = Text(app, color="white", grid=[1,2],text="Focus")
space = PushButton(app, grid=[2,0], width=10, height=10, image="/home/pi/TouchCam/icon/100black.png", command=fullscreen)

button2 = PushButton(app, grid=[3,1], width=150, height=150, image="/home/pi/TouchCam/icon/cam.png", command=capture_image)
text2 = Text(app, color="white", grid=[3,2],text="Image")
space2 = PushButton(app, grid=[4,0], width=10, height=10, image="/home/pi/TouchCam/icon/100black.png", command=long_preview)


button3 = PushButton(app, grid=[5,1], width=150, height=150, image="/home/pi/TouchCam/icon/vid.png", command=video_capture)
text2 = Text(app, color="white", grid=[5,2],text="HD 30s")
space3 = PushButton(app, grid=[6,0], width=10, height=10, image="/home/pi/TouchCam/icon/100black.png", command=long_preview)


button4 = PushButton(app, grid=[7,1], width=150, height=150, image="/home/pi/TouchCam/icon/lapse.png", command=burst)
text3 = Text(app, color="white", grid=[7,2],text="Burst")
space4 = PushButton(app, grid=[8,0], width=10, height=10, image="/home/pi/TouchCam/icon/100black.png", command=long_preview)


button5 = PushButton(app, grid=[1,3], width=150, height=150, image="/home/pi/TouchCam/icon/self.png", command=lapse)
text4 = Text(app, color="white", grid=[1,4],text="1h 60pix")
button6 = PushButton(app, grid=[3,3], width=150, height=150, image="/home/pi/TouchCam/icon/long.png", command=split_hd_30m)
text2 = Text(app, color="white", grid=[3,4],text="HD 30m in 5s")
button7 = PushButton(app, grid=[5,3], width=150, height=150, image="/home/pi/TouchCam/icon/drop.png", command=upload)
text3 = Text(app, color="white", grid=[5,4],text="Upload")
button8 = PushButton(app, grid=[7,3], width=150, height=150, image="/home/pi/TouchCam/icon/del.png", command=clear)
text4 = Text(app, color="white", grid=[7,4],text="Clear Folder")

busy = Window(app, bg="red",  height=100, width=800, title="busy")

# app.tk.attributes("-fullscreen", True)
busy.hide()
app.display()