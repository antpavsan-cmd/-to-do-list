from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
<<<<<<< HEAD

=======
import json
import os
>>>>>>> e5835b8 (добавлен скролл, и еще куча всего)
class App(App):
	def build(self):
		Window.clearcolor = (0.5,0.5,0.5,1)
		self.button_adds = 0
		self.layout_main = BoxLayout(orientation="vertical",spacing=10,padding=10)
		self.button = Button(text="новый ряд",size_hint=(1,None),height=200)
<<<<<<< HEAD
		self.button.bind(on_press=self.button_pressed)
		self.label_top = Label(text="заметки",size_hint=(1,None),height=50)
		self.layout_main.add_widget(self.label_top,index=10)
		self.layout_main.add_widget(self.button)
		return self.layout_main
	def button_pressed(self,instance):
		new_layout = BoxLayout(orientation="horizontal",spacing=5,padding=5,size_hint=(1,None),height=200)
		checkbox=CheckBox(size_hint=(None,None),width=100,height=200)
		new_layout.add_widget(checkbox)
		checkbox.bind(active=lambda checkbox,value: self.checkbox_pressed(new_layout,value))
		new_layout.add_widget(TextInput(multiline=True))
=======
		self.button.bind(on_press=self.create_row)
		self.label_top = Label(text="заметки",size_hint=(1,None),height=50)
		self.layout_main.add_widget(self.label_top,index=10)
		self.layout_main.add_widget(self.button)
		self.save_load()
		return self.layout_main
	def save_load(self):
		if not os.path.exists("data.json"):
			return
		with open("data.json","r",encoding = "utf-8") as f:
			data = json.load(f)
		for task in data:
			self.create_row(text=task["text"],done=task["done"])
	def save(self):
		data = [ ]
		for row in self.layout_main.children:
			if isinstance(row,BoxLayout):
						text = " "
						done = False
						for widget in row.children:
							if isinstance(widget,CheckBox):
								done = widget.active
							if isinstance(widget,TextInput):
								text = widget.text			
						data.append({
						"text": text,
						"done": done
						})
		with open("data.json","w",encoding = "utf-8") as f:
			json.dump(data,f,indent = 4,ensure_ascii=False)
	def create_row(self,instance=None,text=" ",done=False):
		new_layout = BoxLayout(orientation="horizontal",spacing=5,padding=5,size_hint=(1,None),height=200)
		checkbox=CheckBox(size_hint=(None,None),width=100,height=200)
		checkbox.active = done
		new_layout.add_widget(checkbox)
		checkbox.bind(active=lambda checkbox,value: self.checkbox_pressed(new_layout,value))
		textinput = TextInput(text=text,multiline=True)
		new_layout.add_widget(textinput)
>>>>>>> e5835b8 (добавлен скролл, и еще куча всего)
		self.layout_main.add_widget(new_layout)
		self.button_adds +=1
		if self.button_adds >= 10:
			self.layout_main.remove_widget(self.button)
<<<<<<< HEAD
	def checkbox_pressed(self,layout,value):
		if value:
			if not hasattr(layout,'button_del'):
				layout.button_del =Button(text='удалить строку')
=======
		self.save()
	def checkbox_pressed(self,layout,value):
		if value:
			if not hasattr(layout,'button_del'):
				layout.button_del =Button(text='удалить строку',size_hint=(None,1),width=325)
>>>>>>> e5835b8 (добавлен скролл, и еще куча всего)
			layout.button_del.bind(on_press=lambda instance: self.del_row(instance,layout))
			layout.add_widget(layout.button_del)
		else:
			if hasattr(layout,'button_del'):
				if layout.button_del in layout.children:
					layout.remove_widget(layout.button_del)
	def del_row(self,instance,layout):
		self.button_adds -= 1
		self.layout_main.remove_widget(layout)
		if self.button_adds <= 10 and self.button not in self.layout_main.children:
			self.layout_main.add_widget(self.button,index=9)
<<<<<<< HEAD
=======
		self.save()
>>>>>>> e5835b8 (добавлен скролл, и еще куча всего)
if __name__ =='__main__':
	App().run()