import matplotlib
matplotlib.use('GTK3Agg')  # or 'GTK3Cairo'
import matplotlib.pyplot as plt
from random import randrange
import numpy as np
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk

from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure

#==================================================================================================
win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.set_default_size(1000, 1000)
win.set_title("Embedding in GTK")


sw = Gtk.ScrolledWindow()
#win.add(sw)
# A scrolled window border goes outside the scrollbars and viewport
sw.set_border_width(10)

win.fullscreen()



# now let's add a button to the toolbar
button = Gtk.Button(label='ACTION')
button.show()
button.connect('clicked', lambda button: print('hi mom'))


# now let's add a widget to the vbox
label = Gtk.Label()
label.set_markup(' | Benha ventilator |')
# label.show()

label_m = Gtk.Label()
label_a = Gtk.Label()

m_ox = Gtk.Label()
m_peep = Gtk.Label()
m_rr = Gtk.Label()
m_flow = Gtk.Label()
m_i = Gtk.Label()
m_e = Gtk.Label()

a_ox = Gtk.Label()
a_peep = Gtk.Label()
a_flow = Gtk.Label()
a_pressur = Gtk.Label()
a_volume = Gtk.Label()



#adding a spinButton FOR O2
ad = Gtk.Adjustment(value=0, lower=0, upper=100, step_increment=1, page_increment=0, page_size=0)
# a spin button for integers (digits=0)
spin = Gtk.SpinButton(adjustment=ad, climb_rate=1, digits=0)
spin.show()
O2 = Gtk.Label(label="O2")
O2.show()

#adding a spinButton FOR TOTAL FLOW
ad1 = Gtk.Adjustment(value=0, lower=0, upper=100, step_increment=1, page_increment=0, page_size=0)
# a spin button for integers (digits=0)
spin1 = Gtk.SpinButton(adjustment=ad1, climb_rate=1, digits=0)
spin1.show()
Tflow = Gtk.Label(label="Total flow")
Tflow.show()

#adding a spinButton FOR RR
ad2 = Gtk.Adjustment(value=0, lower=0, upper=100, step_increment=1, page_increment=0, page_size=0)
# a spin button for integers (digits=0)
spin_rr = Gtk.SpinButton(adjustment=ad2, climb_rate=1, digits=0)
spin_rr.show()
RR = Gtk.Label(label="RR")
RR.show()

adx = Gtk.Adjustment(value=0, lower=0, upper=100, step_increment=1, page_increment=0, page_size=0)
# a spin button for integers (digits=0)
peep = Gtk.SpinButton(adjustment=adx, climb_rate=1, digits=0)
peep.show()
peep_text = Gtk.Label(label="peep")
peep_text.show()

#adding a spinButton FOR TOTAL FLOW
ady = Gtk.Adjustment(value=0, lower=0, upper=100, step_increment=1, page_increment=0, page_size=0)
# a spin button for integers (digits=0)
pmax = Gtk.SpinButton(adjustment=ady, climb_rate=1, digits=0)
pmax.show()
pmax_text = Gtk.Label(label="PMAX")
pmax_text.show()


#comboboxText
modes = [
            "pressure control",
            "A/C",
            "SMIV",
        ]
modes_combo = Gtk.ComboBoxText()
#currency_combo.set_entry_text_column(0)
# modes_combo.connect("changed", V_modes)
vmodes = Gtk.Label(label="MODE")
vmodes.show()
modes_combo.show()
for mode in modes:
    modes_combo.append_text(mode)

#comboboxText for i:e
inspiration = [
            "1",
            "2",
            "3",
            "4",
        ]
in_combo = Gtk.ComboBoxText()
#currency_combo.set_entry_text_column(0)
# modes_combo.connect("changed", V_modes)
INS = Gtk.Label(label="I")
INS.show()
in_combo.show()
for s in inspiration:
    in_combo.append_text(s)


#comboboxText for i:e
exspiration = [
            "1",
            "2",
            "3",
            "4",
        ]
ex_combo = Gtk.ComboBoxText()
#currency_combo.set_entry_text_column(0)
# modes_combo.connect("changed", V_modes)
EXS = Gtk.Label(label="E")
EXS.show()
ex_combo.show()
for s in exspiration:
    ex_combo.append_text(s)

# a vertical separator
v1 = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
v1.show()


#add a grid
grid = Gtk.Grid(column_spacing = 25)

grid.show()
grid.add(O2)
grid.attach_next_to(spin, O2, Gtk.PositionType.BOTTOM, 1, 2)
grid.attach(Tflow, 1, 0, 1,1)
grid.attach_next_to(spin1, Tflow, Gtk.PositionType.BOTTOM, 1, 1)
grid.attach(v1, 2, 0, 1,2)

grid.attach(RR, 3, 0, 1,1)
grid.attach_next_to(spin_rr, RR, Gtk.PositionType.BOTTOM, 1, 1)
# grid.attach(vmodes, 4, 0, 1,1)
# grid.attach_next_to(modes_combo, vmodes, Gtk.PositionType.BOTTOM, 1, 1)

grid.attach(pmax_text, 5, 0, 1,1)
grid.attach_next_to(pmax,pmax_text, Gtk.PositionType.BOTTOM, 1, 1)
grid.attach(peep_text, 6, 0, 1,1)
grid.attach_next_to(peep,peep_text, Gtk.PositionType.BOTTOM, 1, 1)
grid.attach(INS, 7, 0, 1,1)
grid.attach_next_to(in_combo,INS, Gtk.PositionType.BOTTOM, 1, 1)
grid.attach(EXS, 8, 0, 1,1)
grid.attach_next_to(ex_combo,EXS, Gtk.PositionType.BOTTOM, 1, 1)


#===============================================================styles
vmodes.set_markup("<span font_desc='Tahoma bold 15' color='red' >MODE</span>")
label.set_markup("<span font_desc='Tahoma bold 15' color='blue' >| BENHA ventilator |</span>")

O2.set_markup("<span font_desc='Tahoma bold 20' color='GREEN' >OXYGEN</span>")
Tflow.set_markup("<span font_desc='Tahoma bold 20' color='GREEN' >T-FLOW</span>")
RR.set_markup("<span font_desc='Tahoma bold 20' color='GREEN' >RR</span>")
peep_text.set_markup("<span font_desc='Tahoma bold 20' color='GREEN' >PEEP</span>")
pmax_text.set_markup("<span font_desc='Tahoma bold 20' color='GREEN' >PMAX</span>")
INS.set_markup("<span font_desc='Tahoma bold 20' color='GREEN' >I</span>")
EXS.set_markup("<span font_desc='Tahoma bold 20' color='GREEN' >E</span>")

label_m.set_markup("<span font_desc='Tahoma bold 20' color='black' >MONITORED</span>")
label_a.set_markup("<span font_desc='Tahoma bold 20' color='black' >ADJUSTED</span>")

m_ox.set_markup("<span font_desc='Tahoma bold 20' color='blue' >OXYGEN:</span>" )
m_peep.set_markup("<span font_desc='Tahoma bold 20' color='blue' >PEEP:</span>")
m_rr.set_markup("<span font_desc='Tahoma bold 20' color='blue' >RR:</span>")
m_flow.set_markup("<span font_desc='Tahoma bold 20' color='blue' >FLOW:</span>")
m_i.set_markup("<span font_desc='Tahoma bold 20' color='blue' >I/E:</span>")

a_ox.set_markup("<span font_desc='Tahoma bold 20' color='red' >OXYGEN:</span>" )
a_peep.set_markup("<span font_desc='Tahoma bold 20' color='red' >PEEP:</span>")
a_flow.set_markup("<span font_desc='Tahoma bold 20' color='red' >FLOW:</span>")
a_pressur.set_markup("<span font_desc='Tahoma bold 20' color='red' >PRESSURE:</span>")
a_volume.set_markup("<span font_desc='Tahoma bold 20' color='red' >VOLUME:</span>")



button.set_size_request(800, 0)
modes_combo.set_size_request(100, 70)
v1.set_size_request(100, 100)
spin.set_size_request(100, 100)
spin1.set_size_request(100, 100)
spin_rr.set_size_request(100, 100)
pmax.set_size_request(100, 100)
peep.set_size_request(100, 100)
ex_combo.set_size_request(100, 100)
in_combo.set_size_request(100, 100)

v1.override_background_color(0, Gdk.RGBA(   0,1,0  ))
#-----------------------------------top
box_top = Gtk.Box()
box_top.pack_start(vmodes, False, True, 0)
box_top.pack_start(modes_combo, False, True, 0)
box_top.pack_start(label, False, True, 30)
box_top.pack_start(button, False, True,0)

#===================================

box_r = Gtk.Box(orientation='vertical')
box_r.pack_start(box_top, False, True, 0)
box_r.pack_start(sw, True, True, 0)
box_r.pack_start(grid, False, True, 0)

#===================================
box_a = Gtk.Box(orientation='vertical',spacing =50)
box_a.pack_start(label_a, False, True, 20)
box_a.pack_start(a_ox, False, True, 0)
box_a.pack_start(a_peep, False, True, 0)
box_a.pack_start(a_pressur, False, True, 0)
box_a.pack_start(a_flow, False, True, 0)
box_a.pack_start(a_volume, False, True, 0)

#===================================
box_m = Gtk.Box(orientation='vertical',spacing=50)
box_m.pack_start(label_m, False, True, 20)
box_m.pack_start(m_ox, False, True, 0)
box_m.pack_start(m_peep, False, True, 0)
box_m.pack_start(m_rr, False, True, 0)
box_m.pack_start(m_flow, False, True, 0)
box_m.pack_start(m_i, False, True, 0)

#====================================
box_main = Gtk.Box(homogeneous=False , spacing = 20)
box_main.pack_start(box_r, True, True, 0)
box_main.pack_end(box_m, False, False, 0)
box_main.pack_end(box_a, False, False, 0)

box_main.show()
win.add(box_main)




