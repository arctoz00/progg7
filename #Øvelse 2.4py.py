#Øvelse 2.4

from machine import Pin
from rotary_encoder import RotaryEncoder

class RotaryCallbackManager:
    def __init__(self, pin):
        self.encoder = RotaryEncoder(pin, pin)
        self.callbacks = []

    def add_callback(self, text, callback):
        self.callbacks.append({"text": text, "callback": callback})

    def run_next_callback(self):
        if self.callbacks:
            next_callback = self.callbacks.pop(0)
            next_callback["callback"]()
            print("Running Callback:", next_callback["text"])


def callback1():
    print("Callback 1")

def callback2():
    print("Callback 2")

def callback3():
    print("Callback 3")


ROTARY_ENCODER_PIN = 2


manager = RotaryCallbackManager(ROTARY_ENCODER_PIN)


manager.add_callback("Callback 1", callback1)
manager.add_callback("Callback 2", callback2)
manager.add_callback("Callback 3", callback3)


while True:
    if some_condition: 
        manager.run_next_callback()
