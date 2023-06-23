from guizero import App,Text,PushButton,Slider,TextBox,TitleBox
from collections import namedtuple
import numpy as np
import os
import time


# lpfParam = namedtuple('lpfParam',['yn','yn_1','a'])
lpfHVbat = np.array((0.0,0.0,0.94))

def error_handler(err):
    if err == 1:
        print('Error ' + str (err))

def update_tbHVbat():
    tbHVbat.value = int(tbHVbat.value) + 1

def update_tbLSAbat():
    tbLSAbat.value = int(tbLSAbat.value) + 2

def update_tbBikeState():
    tbBikeState.value = int(tbBikeState.value) + 1

def update_tbHVBatCurr():
    tbHVBatCurr.value = int(tbHVBatCurr.value) + 4


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(lpfHVbat)
    app = App(title= "ION M1S Realtime Diagnostics",height=600,width=1024,layout="grid")
    # titlebox = TitleBox(app, "ION M1S Bike RTMon",grid=[0,0])

    #HV bat voltage output
    lblHVbat = Text(app, text='HV Bat Voltage ',grid=[0,1],size=32,align="left")
    tbHVbat = TextBox(app, text='0',grid=[1,1])
    tbHVbat.set_text_size(tbHVbat,32)
    tbHVbat.repeat(250,update_tbHVbat)

    #LSA voltage output
    lblLSAbat = Text(app, text='LSA Bat',grid=[0,2],size=32,align="left")
    tbLSAbat = TextBox(app, text='0',grid=[1,2])
    tbLSAbat.set_text_size(tbLSAbat,32)
    tbLSAbat.repeat(500,update_tbLSAbat)

    #Bike state output
    lblBikeState = Text(app, text='Bike State ',grid=[0,3],size=32,align="left")
    tbBikeState = TextBox(app, text='0',grid=[1,3])
    tbBikeState.set_text_size(tbBikeState,32)
    tbBikeState.repeat(100,update_tbBikeState)

    #HV bat current output
    lblHVBatCurr = Text(app, text='HV Bat Current ',grid=[0,4],size=32,align="left")
    tbHVBatCurr = TextBox(app, text='0',grid=[1,4])
    tbHVBatCurr.set_text_size(tbHVBatCurr,32)
    tbHVBatCurr.repeat(1000,update_tbHVBatCurr)




    app.display()
    # message = Text(app, text= "hello world")
    error_handler(1)
