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
        self.label = Label(pos_hint={'center_x': 0.1, 'center_y': 0.9})
        self.image = Image()
        self.add_widget(self.image)
        self.add_widget(self.label)

        self._update_image(self._files.get_next_image())

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _update_image(self, path):
        self.image.source = path
        self.label.text = self._files.get_date()

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode)
        if keycode[1] == "q":
            App.get_running_app().stop()
        if keycode[1] == "right":
            self._update_image(self._files.get_next_image())
        if keycode[1] == "left":
            self._update_image(self._files.get_prev_image())

        return True

class CullApp(App):
    def build(self):
        return Photo()

if __name__ == "__main__":
    CullApp().run()
