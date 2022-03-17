import sys

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image

class Photo(Image):
    def __init__(self, **kwargs):
        super(Photo, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode)
        if keycode[1] == "q":
            App.get_running_app().stop()
            
        return True

class CullApp(App):
    def build(self):
        return Photo(source="IMG_3838_80d.cr2")

if __name__ == "__main__":
    CullApp().run()
