from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def build(self):
        self.screen = MDScreen()

        self.label = MDLabel(text='Android app development', halign='center', pos_hint={'center_x':0.5, 'center_y':0.5})
        self.screen.add_widget(self.label)

        return self.screen

if __name__=='__main__':
    MyApp().run()