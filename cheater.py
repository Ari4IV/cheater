from pynput.keyboard import Key, Controller
from pynput.keyboard import Listener

import time

qwerty = Controller()
t_end = time.time() + 3

def main():

        def on_press(key):
            global t_end
            time.sleep(0.5)
            qwerty.release(key)
            if t_end < time.time():
                print('time out!')
                return False

        with Listener(on_press=on_press) as listener:
            listener.join()

if __name__ == '__main__':
    main()