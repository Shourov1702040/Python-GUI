from kivymd.app import MDApp
from kivy.lang.builder import Builder

class MyApp(MDApp):
	def build(self):
		
		self.screen = Builder.load_file('03_ways_of _using_kivy.kv')

		return self.screen

	def button_press(self):
		print("My buttons pressed")

if __name__=='__main__':
	MyApp().run()
