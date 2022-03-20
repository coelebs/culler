#!/usr/bin/env python
import os

from images import RawFolder

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class Photo(FloatLayout):
    def __init__(self, **kwargs):
        super(Photo, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._files = RawFolder()
        self.date = Label(pos_hint={'center_x': 0.1, 'center_y': 0.9})
        self.date.font_size = 24
        self.stars = Label(pos_hint={'center_x': 0.9, 'center_y': 0.9}, size_hint=(0.1, 0.1))
        self.stars.font_size = 24
        self.stars.color = (1, 1, 1, 1)
        self.imagewidget = Image()
        self.add_widget(self.imagewidget)
        self.add_widget(self.date)
        self.add_widget(self.stars)
        self.image = self._files.get_next_image()
        self._update_image()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _update_image(self):
        self.imagewidget.source = str(self.image)
        self.date.text = self.image.get_date()
        self.stars.text = "%s STARS" % self.image.rating()

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode)
        if keycode[1] == "q":
            App.get_running_app().stop()
        if keycode[1] == "right":
            self.image = self._files.get_next_image()
            self._update_image()
        if keycode[1] == "left":
            self.image = self._files.get_prev_image()
            self._update_image()
        if keycode[1] >=  "1" and keycode[1] <= "5":
            self.stars.text = "%s STAR" % keycode[1]
            self.image.rate(keycode[1])

        return True

class CullApp(App):
    def build(self):
        return Photo()

if __name__ == "__main__":
    CullApp().run()
