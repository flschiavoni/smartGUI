# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import components
from components.stringfield import StringField
from components.intfield import IntField
from components.commentfield import CommentField
from components.colorfield import ColorField
from components.floatfield import FloatField

from components.constants import *


component_list = {
           HARPIA_STRING:  StringField,
           HARPIA_COMMENT: CommentField,
           HARPIA_INT:     IntField,
           HARPIA_COLOR:   ColorField,
           HARPIA_FLT:     FloatField
           }

class PropertyWindow(Gtk.Dialog):

    def __init__(self, plugin, parent):
        self.plugin = plugin
        self.properties = {}
        Gtk.Dialog.__init__(self, "Properties", parent)

        self.notebook = Gtk.Notebook()
        self.vbox.set_homogeneous(False)
        self.vbox.add(self.notebook)

        #Properties tab
        property_box = Gtk.VBox(False, 0)
        self.notebook.append_page(property_box, Gtk.Label("Properties"))

        #Search plugin properties to create GUI
        for component in self.plugin.get_properties() :
            field = self._generate_field(
                        component, self.plugin.get_properties()[component])
            property_box.add(field)

        #Help Tab
        help_box = Gtk.VBox(True, 0)
        self.notebook.append_page(help_box, Gtk.Label("Help"))
        
        scrolled_window = Gtk.ScrolledWindow()

        help_text = Gtk.TextView()
        help_text.set_left_margin(10)
        help_text.set_right_margin(10)
        help_text.set_wrap_mode(Gtk.WrapMode.WORD)

        text_buffer = help_text.get_buffer()
        text_buffer.set_text(plugin.getHelp())
        scrolled_window.add(help_text)

        help_box.add(scrolled_window)

        #Buttons
        hbox = Gtk.HBox(True, 0)
        self.vbox.add(hbox)

        button1 = Gtk.Button("Ok")
        button1.connect("clicked", self.on_ok_clicked, self)
        hbox.add(button1)

        button2 = Gtk.Button("Cancelar")
        button2.connect("clicked", self.on_cancel_clicked, self)
        hbox.add(button2)

        self.vbox.show_all()

    def on_ok_clicked(self, widget, data):
        # It is time to look for values
        self._recursive_search(self)
        # Onde we have a returnable dictionary, call the callback method
        self.plugin.set_properties(self.properties)
        self.destroy()

    def on_cancel_clicked(self, widget, data):
        self.destroy()

    def _recursive_search(self, container):
        for widget in container.get_children() :
            #If widget is a container, search inside it
            if isinstance(widget, Gtk.Container) :
                self._recursive_search(widget)
            # Onde a component is found, search for it on the component list
            if widget.get_name() in self.plugin.get_properties() :
                self.properties[widget.get_name()] = widget.get_value()
    
    def _generate_field(self, component_key, component_attributes):
        type_ = component_attributes["type"]
        # zhu li, do the thing!
        #Creates a field based on the component list types
        field = component_list[type_](component_attributes)
        field.set_name(component_key) #Define widget name
        return field
    
