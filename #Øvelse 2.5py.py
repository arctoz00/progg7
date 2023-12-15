#Øvelse 2.5

from machine import Pin
from rotary_encoder import RotaryEncoder

class RotaryMenu:
    def __init__(self, pin):
        self.encoder = RotaryEncoder(pin, pin)  
        self.menu_items = ["Option 1", "Option 2", "Option 3"]
        self.selected_index = 0

    def display_menu(self):
        for i, item in enumerate(self.menu_items):
            if i == self.selected_index:
                print("->", item)
            else:
                print("   ", item)

    def run_selected_option(self):
        print("Selected:", self.menu_items[self.selected_index])

    def navigate_menu(self):
        direction = self.encoder.get_direction()
        if direction == 1:
            self.selected_index = (self.selected_index + 1) % len(self.menu_items)
        elif direction == -1:
            self.selected_index = (self.selected_index - 1) % len(self.menu_items)


ROTARY_ENCODER_PIN = 2


menu = RotaryMenu(ROTARY_ENCODER_PIN)


while True:
    menu.display_menu()
    menu.navigate_menu()
    if some_condition: 
        menu.run_selected_option()
