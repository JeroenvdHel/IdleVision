import kivy
import os

from kivy.clock import Clock

kivy.require('2.0.0')
from kivy.app import App, async_runTouchApp
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        self.start()
        self.counter = 0
        super().__init__(**kwargs)

    def start(self):
        Clock.schedule_interval(self.update_am, 1)

    def update_am(self, dt):
        self.counter += 1
        self.ids.lbl_am_counter.text = f'You have [b][size=30][color=18dc2c]' \
                                       f'{self.counter}[/color][/size][/b] ' \
                                       f'antimatter'
        self.ids.lbl_am_sec_counter.text = f'You are getting [b]{self.counter}[/b] ' \
                                           f'antimatter per second'


class RootWidget(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class IdleVisionApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    # Load custom kivy config file
    Config.read('config/kv-config.ini')

    # Load Kivy template file
    kv = Builder.load_file('kv-files/main.kv')

    IdleVisionApp().run()