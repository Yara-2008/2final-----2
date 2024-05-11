def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_number(randint(0, 5))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    if input.temperature() > 0:
        basic.show_string("Above")
        if input.temperature() > 0:
            basic.show_string("below")
        else:
            basic.show_string("zero")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Mynum
    Mynum += 2
    basic.show_number(Mynum)
input.on_button_pressed(Button.B, on_button_pressed_b)

Mynum = 0
i = 0
basic.show_string("Hello! yara")