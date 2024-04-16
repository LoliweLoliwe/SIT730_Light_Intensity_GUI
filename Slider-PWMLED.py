from gpiozero import PWMLED
import time
from guizero import App, Text, PushButton, ButtonGroup, Slider, TextBox
import sys

red = PWMLED(17)
green = PWMLED(18)
blue = PWMLED(22)

def switch_on1(slider1_value):
    try:
        if clicked.value == "green":
            green.value = int(slider1_value) // 100
    except KeyboardInterrupt:
        GPIO.cleanup()

def switch_on2(slider2_value):
    try:
        if clicked.value == "red":
            red.value = int(slider2_value) // 100
    except KeyboardInterrupt:
        GPIO.cleanup()

def switch_on3(slider3_value):
    try:
        if clicked.value == "blue":
            blue.toggle()
            blue.pulse(fade_in_time=2, fade_out_time=2, n=None, background=True)
            print(slider3_value)
            textbox.value = slider3_value
    except KeyboardInterrupt:
        GPIO.cleanup()

def close_gui():
    blue.off()
    red.off()
    green.off()
    sys.exit()

app = App(title="LED GUI")
Text(app, text = "3 LED's")
clicked = ButtonGroup(app, options=["green", "red", "blue"], horizontal=True)
Text(app, text = "Move the Sliders")

slider1 = Slider(app, command=switch_on1)
slider2 = Slider(app, command=switch_on2)
slider3 = Slider(app, command=switch_on3)
btn3 = PushButton(app, command=close_gui, text="EXIT", width=20, height=5)
textbox = TextBox(app)
#led1_text = Text(app, text = "You have switched on a ")

app.display()