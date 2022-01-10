from kivymd.app import MDApp
from kivy.lang.builder import Builder

class MyApp(MDApp):
	def build(self):
		
		self.screen = Builder.load_file("D:/Working_dir/Programming/Python/KivyMD/04_Layouts.kv")

		return self.screen

if __name__=='__main__':
	MyApp().run()