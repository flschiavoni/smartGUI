#!/usr/bin/env python
 # -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from plugins.erosao import Erosao
from plugins.dilatacao import Dilatacao
from plugins.haar import Haar

from propertywindow import PropertyWindow

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        hbox = Gtk.HBox(True, 0)
        self.add(hbox)

        erosao = Erosao()
        self.button = Gtk.Button(label="Erosão")
        self.button.connect("clicked", self.on_button_clicked, erosao)
        hbox.add(self.button)

        dilatacao = Dilatacao()
        self.button2 = Gtk.Button(label="Dilatação")
        self.button2.connect("clicked", self.on_button_clicked, dilatacao)
        hbox.add(self.button2)

        haar = Haar()
        self.button3 = Gtk.Button(label="haar")
        self.button3.connect("clicked", self.on_button_clicked, haar)
        hbox.add(self.button3)

    def on_button_clicked(self, widget, data):
        PropertyWindow(data, self).show()

if __name__ == "__main__":
    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
