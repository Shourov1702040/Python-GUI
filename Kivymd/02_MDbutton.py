from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton, MDFlatButton, MDRaisedButton, MDRoundFlatButton, MDRectangleFlatButton, MDRectangleFlatIconButton

class MyApp(MDApp):
	def build(self):

		self.screen = MDScreen()

		self.button1 = MDIconButton(icon = 'language-python', pos_hint={'center_x':0.5, 'center_y':0.9}, on_release=self.button_press)
		self.screen.add_widget(self.button1)

		self.button2 = MDFlatButton(text='Flat button', pos_hint={'center_x':0.5, 'center_y':0.8}, on_release=self.button_press)
		self.screen.add_widget(self.button2)

		self.button3 = MDRaisedButton(text='Raised button', pos_hint={'center_x':0.5, 'center_y':0.7}, on_release=self.button_press)
		self.screen.add_widget(self.button3)

		self.button4 = MDRoundFlatButton(text='RoundFlat Button', pos_hint={'center_x':0.5, 'center_y':0.6}, on_release=self.button_press)
		self.screen.add_widget(self.button4)

		self.button5 = MDRectangleFlatButton(text='RectangleFlat Button', pos_hint={'center_x':0.5, 'center_y':0.5}, on_release=self.button_press)
		self.screen.add_widget(self.button5)

		self.button6 = MDRectangleFlatIconButton(text='RectangleFlatIcon Button', pos_hint={'center_x':0.5, 'center_y':0.4}, on_release=self.button_press)
		self.screen.add_widget(self.button6)

		return self.screen

	def button_press(self, args):
		print("My buttons pressed")

if __name__=='__main__':
	MyApp().run()