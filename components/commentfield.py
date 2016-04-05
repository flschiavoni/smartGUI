import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from components.field import Field
from constants import *

class CommentField(Field, Gtk.VBox):

    def __init__(self, data):
        if not isinstance(data,dict):
            return
        Gtk.VBox.__init__(self)
        self.set_homogeneous(False)
        self.set_spacing(10)
        scrolled_window = Gtk.ScrolledWindow()

        scrolled_window.set_min_content_height(data["height"])
        scrolled_window.set_min_content_width(data["width"])

        label = Gtk.Label(data["name"])
        self.add(label)

        self.field = Gtk.TextView()
        self.field.set_left_margin(10)
        self.field.set_right_margin(10)
        self.field.set_wrap_mode(Gtk.WrapMode.WORD)

        self.text_buffer = self.field.get_buffer()
        self.text_buffer.set_text(data["value"])
        scrolled_window.add(self.field)

        self.add(scrolled_window)
        self.show_all()

    def get_type(self):
        return HARPIA_COMMENT
        
    def get_value(self):
        return self.text_buffer.get_text(
                        self.text_buffer.get_start_iter(),
                        self.text_buffer.get_end_iter(),
                        True)
