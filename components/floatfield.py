#!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from components.field import Field
from constants import *

class FloatField(Field, Gtk.HBox):

    def __init__(self, data):
        if not isinstance(data,dict):
            return
        Gtk.HBox.__init__(self, True)
        label = Gtk.Label(data["name"])
        self.add(label)

	#coloca os valores em variáveis e passa as que existem pro Adjustment
	#Se os caras não existirem, ERRORFIELD NELES!!!
        adjustment = Gtk.Adjustment(value=data["value"],
                                lower=data["lower"],
                                upper=data["upper"],
                                step_incr=data["step"],
                                page_incr=0,
                                page_size=0)
        self.field = Gtk.SpinButton()
        self.field.configure(adjustment, 0.0, data["digits"])
        self.field.set_value(data["value"])
        self.add(self.field)
        self.show_all()

    def get_type(self):
        return HARPIA_FLOAT

    def get_value(self):
        return self.field.get_value()
