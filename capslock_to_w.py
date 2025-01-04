import time
from pynput import keyboard
from pynput.keyboard import Controller

# Initialize the key controller
key_controller = Controller()

# Configurable timing
double_press_interval = 0.3  # Maximum time (seconds) between double presses

# State tracking
last_press_time = 0
press_count = 0

def on_press(key):
    global last_press_time, press_count

    try:
        # Check if the Caps Lock key is pressed
        if key == keyboard.Key.caps_lock:
            current_time = time.time()
            
            # If the time since the last press is within the double press interval
            if current_time - last_press_time <= double_press_interval:
                press_count += 1
            else:
                press_count = 1  # Reset to 1 if the time has exceeded the interval

            last_press_time = current_time

            # If double press detected, type 'w'
            if press_count == 2:
                key_controller.type('w')
                press_count = 0  # Reset the counter after typing 'w'
    except AttributeError:
        pass

def on_release(key):
    # Exit the program if the Escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
