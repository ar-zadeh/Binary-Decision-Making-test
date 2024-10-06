
import webbrowser
import csv
import time
import pyautogui
from pynput import keyboard, mouse
import os
from opengaze import *
flag = True
# Keyboard listener
def on_keyboard_press(key):
    global flag
    with open('keyboard_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Keyboard Press', time.time(),str(key)])
    
    if key == keyboard.Key.esc:
    # Terminate the code
        return  False

def on_keyboard_release(key):
    with open('keyboard_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Keyboard Release',time.time(), str(key)])

# Mouse listener
def on_mouse_move(x, y):
    with open('mouse_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        print(['Mouse Move', x, y])
        writer.writerow(['Mouse Move', x, y])

def on_mouse_click(x, y, button, pressed):
    with open('mouse_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Mouse Click' if pressed else 'Mouse Release', x, y, button])
    
    if pressed:
        # Capture screenshot
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_file = f'screenshot_{timestamp}.png'
        pyautogui.screenshot(screenshot_file)

# Create listeners
gazetracker = GazePoint()
new = 2 # open in a new tab, if possible

# open an HTML file on my own (Windows) computer

url = f"file:\\{os.getcwd()}\\index.html"
webbrowser.open(url,new=new)
keyboard_listener = keyboard.Listener(on_press=on_keyboard_press, on_release=on_keyboard_release)
mouse_listener = mouse.Listener(on_move=on_mouse_move, on_click=on_mouse_click)

# Start listeners
keyboard_listener.start()
mouse_listener.start()
print("done")
# Keep the program running until interrupted
start = time.time()

print("done")

ctime = time.time()-start
while True:
    with open('gaze_pos.csv', 'a', newline='') as file:
        x,y = gazetracker.get_gaze_position()
        writer = csv.writer(file)
        print([ctime, x, y])
        writer.writerow([ctime, x, y])
