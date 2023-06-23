from guizero import App,Text
import os
import time

def error_handler(err):
    if err == 1:
        print('Error ' + str (err))

def update_lbl():
    message.value = int(message.value) + 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = App(title= "ION M1S Realtime Diagnostics",height=768,width=1366)
    message = Text(app, text= '0')

    message.repeat(1000,update_lbl)
    app.display()
    # message = Text(app, text= "hello world")
    error_handler(1)
