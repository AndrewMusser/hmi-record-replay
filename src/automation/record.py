import json
import time
from pynput import mouse

# List to store recorded events
events = []

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

# Set up mouse listener
mouse_listener = mouse.Listener(on_click=on_click)

# Start the listeners
mouse_listener.start()

# Wait for the listener to stop (blocking)
mouse_listener.join()

# Save the events to a JSON file
with open('events.json', 'w') as f:
    json.dump(events, f, indent=4)

print("Recording saved to events.json")
