#Øvelse 2.3

from machine import Pin
from rotary_encoder import RotaryEncoder


ROTARY_A_PIN = 2
ROTARY_B_PIN = 3


encoder = RotaryEncoder(ROTARY_A_PIN, ROTARY_B_PIN)


while True:
    direction = encoder.get_direction()
    print("Rotation Direction:", direction)
