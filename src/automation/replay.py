import json
import time
from pynput import mouse, keyboard

# Initialize controllers for replay
mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

# Load the events from the JSON file
with open('events.json', 'r') as f:
    events = json.load(f)

# Replay the recorded events
start_time = events[0]['time']  # Get the time of the first event

for event in events:
    # Calculate the delay based on the time difference between events
    time.sleep(event['time'] - start_time)
    start_time = event['time']

    if event['type'] == 'mouse_click':
        # Move the mouse to the recorded position and click/release
        mouse_controller.position = (event['x'], event['y'])
        if event['pressed']:
            mouse_controller.press(mouse.Button[event['button'].split('.')[1]])
        else:
            mouse_controller.release(mouse.Button[event['button'].split('.')[1]])
    elif event['type'] == 'key_press':
        try:
            if len(event['key']) == 1:  # Printable character
                keyboard_controller.press(event['key'])
            else:
                keyboard_controller.press(getattr(keyboard.Key, event['key'].split('.')[1]))
        except AttributeError:
            pass  # Handle special keys (like Ctrl) here if needed
    elif event['type'] == 'key_release':
        try:
            if len(event['key']) == 1:  # Printable character
                keyboard_controller.release(event['key'])
            else:
                keyboard_controller.release(getattr(keyboard.Key, event['key'].split('.')[1]))
        except AttributeError:
            pass  # Handle special keys (like Ctrl) here if needed

print("Replay finished.")
