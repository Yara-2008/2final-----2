input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Happy)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showNumber(randint(0, 5))
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    if (input.temperature() > 0) {
        basic.showString("Above")
        if (input.temperature() > 0) {
            basic.showString("below")
        } else {
            basic.showString("zero")
        }
        
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Mynum += 2
    basic.showNumber(Mynum)
})
let Mynum = 0
let i = 0
basic.showString("Hello! yara")
