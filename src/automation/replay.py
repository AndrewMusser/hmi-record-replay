import json
import time
from pynput import mouse, keyboard

# Initialize controllers for replay
mouse_controller = mouse.Controller()

# Load the events from the JSON file
with open('events.json', 'r') as f:
    events = json.load(f)

# Replay the recorded events
start_time = events[0]['time']  # Get the time of the first event

for event in events:
    # Calculate the delay based on the time difference between events
    time.sleep(event['time'] - start_time)
    start_time = event['time']

    # Move the mouse to the recorded position and click/release
    mouse_controller.position = (event['x'], event['y'])
    if event['pressed']:
        mouse_controller.press(mouse.Button['left'])
    else:
        mouse_controller.release(mouse.Button['left'])

print("Replay finished.")
