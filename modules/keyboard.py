
import pynput
from pynput import keyboard


class Keyboard:
    def __init__(self,):
        self.is_pressed = False
        self.already_used = False

        listener = keyboard.Listener(
            on_press=self.set_good,
            on_release=self.set_bad
        )

        listener.start()

    def is_enter_just_pressed(self):

        if self.is_pressed and not self.already_used:
            self.already_used = True
            return True
        return False
    
    def set_good(self, key):
        if key == keyboard.Key.enter:
            self.is_pressed = True
            

    def set_bad(self, key):
        if key == keyboard.Key.enter:
            self.is_pressed = False
            self.already_used = False
    
    def update(self):
        return
        '''
        if not keyboard.is_pressed("enter"):
            self.already_used = False
            self.is_pressed = False
        else:
            self.is_pressed = True
``      '''

