import json
import time
from pynput import mouse, keyboard

# List to store recorded events
events = []

listening = True

# This function will be called whenever a mouse click is detected
def on_click(x, y, button, pressed):
    if str(button) == 'Button.right':
        return False
    else:
        event = {
            'type': 'mouse_click',
            'x': x,
            'y': y,
            'button': str(button),
            'pressed': pressed,
            'time': time.time()  # Record the time of the event
        }
        events.append(event)
        print(f"Mouse {'pressed' if pressed else 'released'} at ({x}, {y}) with {button}")

# This function will be called whenever a key is pressed
def on_press(key):
    try:
        event = {
            'type': 'key_press',
            'key': key.char,  # For printable characters
            'time': time.time()  # Record the time of the event
        }
    except AttributeError:
        event = {
            'type': 'key_press',
            'key': str(key),  # For special keys like 'Ctrl', 'Alt', etc.
            'time': time.time()  # Record the time of the event
        }
    events.append(event)
    print(f"Key {key} pressed")

# This function will be called whenever a key is released
def on_release(key):
    event = {
        'type': 'key_release',
        'key': str(key),
        'time': time.time()  # Record the time of the event
    }
    events.append(event)
    print(f"Key {key} released")
    if key == keyboard.Key.esc:
        # Stop listener if Esc is pressed
        print("Stopping the listeners...")
        listening = False
        return False

# Set up mouse and keyboard listeners
mouse_listener = mouse.Listener(on_click=on_click)
# keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the listeners
mouse_listener.start()
# keyboard_listener.start()

print("Got here first!")

# Wait for the listeners to stop (blocking)
mouse_listener.join()
# keyboard_listener.join()

print("Got here again")

# Save the events to a JSON file
with open('events.json', 'w') as f:
    json.dump(events, f, indent=4)

print("Recording saved to events.json")
