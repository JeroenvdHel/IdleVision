from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button


# The kivy App that extends from the App class

class ClockDemo(App):
    count = 0

    def speed_up(self, instance):
        pass

    def build(self):
        self.myLabel = Label(text='Antimatter amount: 0')
        self.myButton = Button(text='Speed up...',
                               on_press=self.speed_up)

        # Start the clock

        Clock.schedule_interval(self.Callback_Clock, 1)


        return self.myLabel

    def Callback_Clock(self, dt):
        self.count = self.count + 1

        self.myLabel.text = f"Antimatter amount {self.count}"


# Run the app

if __name__ == '__main__':
    ClockDemo().run()