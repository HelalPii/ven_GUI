import matplotlib
matplotlib.use('GTK3Agg')  # or 'GTK3Cairo'
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.animation import FuncAnimation
from random import randrange
import numpy as np
import gi
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)

gi.require_version('PangoCairo', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from widgetv2 import *
from gi.repository import Pango
from gi.repository import PangoCairo
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure
import time

#==============================================================================================

# import busio
# import digitalio
# import board
# import adafruit_mcp3xxx.mcp3008 as MCP
# from adafruit_mcp3xxx.analog_in import AnalogIn
# import threading
# import pandas as pd

#================================================================================================
start = time.time()


# # create the spi bus
# spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# # create the cs (chip select)
# cs = digitalio.DigitalInOut(board.D5)
# # create the mcp object
# mcp = MCP.MCP3008(spi, cs)

# def analogread(ch):
#     if ch == 0:
#         ch_analog = AnalogIn(mcp, MCP.P0);
#         volt = ch_analog.voltage;
#     elif ch == 1:
#         ch_analog = AnalogIn(mcp, MCP.P1);
#         volt = ch_analog.voltage;
#     elif ch == 2:
#         ch_analog = AnalogIn(mcp, MCP.P2);
#         volt = ch_analog.voltage;
#     elif ch == 3:
#         ch_analog = AnalogIn(mcp, MCP.P3);
#         volt = ch_analog.voltage;
#     elif ch == 4:
#         ch_analog = AnalogIn(mcp, MCP.P4);
#         volt = ch_analog.voltage;
#     elif ch == 5:
#         ch_analog = AnalogIn(mcp, MCP.P5);
#         volt = ch_analog.voltage;
#     elif ch == 6:
#         ch_analog = AnalogIn(mcp, MCP.P6);
#         volt = ch_analog.voltage;
#     elif ch == 7:
#         ch_analog = AnalogIn(mcp, MCP.P7);
#         volt = ch_analog.voltage;
#
#     return (round(volt, 2))


def sig(arg):
    global y, values1, values2, values3,ox_moni,peep_moni,flow_moni,pressure_moni,v_moni,x,z,s
    #values1.append(analogread(0))
    x=randrange(0,4)
    values1.append(x)
    values1.pop(0)
    #values2.append(analogread(1))
    #values3.append(analogread(2))
    s=randrange(0,4)
    values2.append(s)
    values2.pop(0)
    z=randrange(0,4)
    values3.append(z)
    values3.pop(0)
    y += 1

    # print("samples =", y)


# 3aaaaaaash
def RealtimePloter(arg):
    global y, values1, values2, values3,x,s,z

    CurrentXAxis = np.arange(len(values1) - X_resolution, len(values1), 1)

    line1[0].set_data(CurrentXAxis, np.array(values1[-X_resolution:]))
    ax.axis([CurrentXAxis.min(), CurrentXAxis.max(), -1, 5])

    line2[0].set_data(CurrentXAxis, np.array(values2[-X_resolution:]))
    ax1.axis([CurrentXAxis.min(), CurrentXAxis.max(), -1, 5])

    line3[0].set_data(CurrentXAxis, np.array(values3[-X_resolution:]))
    ax1.axis([CurrentXAxis.min(), CurrentXAxis.max(), -1, 5])

    f.canvas.draw()


    print("time is = ", time.time() - start)
    print("samples = ", y)
    y = 0

def update_state(arg):
    global  s,x,z
    ox_moni.set_markup("<span font_desc='Tahoma bold 15' color='red' >Oxygen: %s</span>" %x)
    peep_moni.set_markup("<span font_desc='Tahoma bold 15' color='red'>peep: %s</span>" %x)
    flow_moni.set_markup("<span font_desc='Tahoma bold 15' color='red'>Flow: %s</span>" %s)
    pressure_moni.set_markup("<span font_desc='Tahoma bold 15' color='red'>pressure: %s</span>" %s)
    v_moni.set_markup("<span font_desc='Tahoma bold 15' color='red'>volume: %s</span>" %z)


def my_timer():
    print ("hiiiiii")

#==============================================================================================callback functions

# main
NUM = 100
TICK = 1
PAN = 10
i = 0
X_resolution = 500
y = 0
x,s,z=0,0,0 # variables to hold the values of the sensors to be monitored

global values1,values2,values3
values1 = [0 for x in range(X_resolution)]
values2 = [0 for x in range(X_resolution)]
values3 = [0 for x in range(X_resolution)]
# ok
xAchse = np.arange(0, 100, 1)
yAchse = np.array([0] * 100)
yAchse1 = np.array([0] * 100)
yAchse2 = np.array([0] * 100)




plt.style.use('Solarize_Light2')
# dark_background    Solarize_Light2     bmh   fivethirtyeight


#win.full_screen_toggle()   # for full screen view




#=========================================================================================
f = Figure(figsize=(5, 4), dpi=100)
ax = f.add_subplot(311)
ax.grid(True)
ax.axis([0, X_resolution, -1.5, 3.5])
line1 = ax.plot(xAchse, yAchse, '-')

ax1 = f.add_subplot(312)
ax1.grid(True)
ax1.axis([0, X_resolution, -1.5, 3.5])
line2 = ax1.plot(xAchse, yAchse1, '-', color='r')

ax2 = f.add_subplot(313)
ax2.grid(True)
ax2.axis([0, X_resolution, -1.5, 3.5])
line3 = ax2.plot(xAchse, yAchse2, '-', color='g')

timer = plt.gcf().canvas.new_timer(interval=900)
timer.add_callback(RealtimePloter, ())
timer2 = plt.gcf().canvas.new_timer(interval=10)
timer2.add_callback(sig, ())
timer3 = plt.gcf().canvas.new_timer(interval=900)
timer3.add_callback(update_state, ())
timer.start()
timer2.start()
timer3.start()

global sw

canvas = FigureCanvas(f)  # a Gtk.DrawingArea
canvas.set_size_request(1000, 1000)
sw.add_with_viewport(canvas)


#=========================================================================================


# vbox.pack_start(label, False, False, 0)
# vbox.pack_start(button, False, False, 0)
# vbox.pack_start(box, False, False, 0)

#win.override_background_color(0, Gdk.RGBA(   1,1,0  ))
win.show_all()
Gtk.main()


#=================================================================================plots and plot window


