from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
import json
import os
class App(App):
	def build(self):
		Window.clearcolor = (0.5,0.5,0.5,1)
		self.scroll = ScrollView(size_hint=(1,1))
		self.layout_label= BoxLayout(orientation="horizontal",spacing=10,padding=1,size_hint=(1,None),height=50)
		self.layout_rows = BoxLayout(orientation="vertical",spacing=1,padding=1,size_hint=(1,None))
		self.layout_rows.bind(minimum_height=self.layout_rows.setter("height"))
		self.scroll.add_widget(self.layout_rows)
		self.layout_top = BoxLayout(orientation="horizontal",spacing=10,padding=1,size_hint=(1,None),height=200)
		self.layout_main = BoxLayout(orientation="vertical",spacing=10,padding=10)
		self.button = Button(text="новый ряд",size_hint=(1,None),height=200)
		self.button.bind(on_press=self.create_row)
		self.clear = Button(text="очистить",size_hint=(1,None),height=200)
		self.clear.bind(on_press=self.remove_all)
		self.save_but = Button(text="сохранить",size_hint=(1,None),height=200)
		self.save_but.bind(on_press=self.save)
		self.label_top = Label(text="заметки",size_hint=(None,None),width=450,height=50)
		self.text_label=(TextInput(text="новое название",multiline=False,size_hint=(None,None),width=450,height=70))
		self.text_label.opacity = 0
		self.text_label.disabled= True
		self.checkbox_label=CheckBox(size_hint=(None,None),width=50,height=50)
		self.checkbox_label.bind(active=self.change_label)
		self.layout_label.add_widget(self.text_label)
		self.layout_label.add_widget(self.label_top)
		self.layout_label.add_widget(self.checkbox_label)
		self.layout_top.add_widget(self.button)
		self.layout_top.add_widget(self.clear)
		self.layout_top.add_widget(self.save_but)
		self.layout_main.add_widget(self.layout_label)
		self.layout_main.add_widget(self.layout_top)
		self.layout_main.add_widget(self.scroll)
		self.save_load()
		return self.layout_main
		#сейв лоад
	def save_load(self):
		if not os.path.exists("data.json"):
			return
		with open("data.json","r",encoding = "utf-8") as f:
			data = json.load(f)
		for task in data:
			self.create_row(text=task["text"],done=task["done"])
			#сейв
	def save(self,instance=None):
		data = [ ]
		for row in reversed(self.layout_rows.children):
			if isinstance(row,BoxLayout):
						text = ""
						done = False
						for widget in row.children:
							if isinstance(widget,CheckBox):
								done = widget.active
							if isinstance(widget,TextInput):
								text = widget.text
						data.append({
						"text": text,
						"done": done,
						})
		with open("data.json","w",encoding = "utf-8") as f:
			json.dump(data,f,indent = 4,ensure_ascii=False)
		#создание рядов
	def create_row(self,instance=None,text="",done=False):
		new_layout = BoxLayout(orientation="horizontal",spacing=5,padding=5,size_hint=(1,None),height=200)
		checkbox=CheckBox(size_hint=(None,None),width=100,height=200)
		checkbox.active = done
		new_layout.add_widget(checkbox)
		checkbox.bind(active=lambda checkbox,value: self.checkbox_pressed(new_layout,value))
		textinput = TextInput(text=text,multiline=True)
		new_layout.add_widget(textinput)
		self.layout_rows.add_widget(new_layout)
		if done:
			self.checkbox_pressed(new_layout,True)
	def checkbox_pressed(self,layout,value):
		if value:
			if not hasattr(layout,'button_del'):
				layout.button_del =Button(text='удалить строку',size_hint=(None,1),width=325)
			layout.button_del.bind(on_press=lambda instance: self.del_row(instance,layout))
			layout.add_widget(layout.button_del)
		else:
			if hasattr(layout,'button_del'):
				if layout.button_del in layout.children:
					layout.remove_widget(layout.button_del)
		#кнопка удалялка
	def del_row(self,instance,layout):
		self.layout_rows.remove_widget(layout)
		self.save()
	# кнопка очистки
	def remove_all(self,instance=None):
		self.layout_rows.clear_widgets()
		#заголовки
	def change_label(self,instance,value):
		if value:
			self.label_top.opacity = 0
			self.label_top.disabled= True
			self.text_label.opacity = 1
			self.text_label.disabled= False
		else:
			self.label_top.text=self.text_label.text
			self.text_label.opacity = 0
			self.text_label.disabled= True
			self.label_top.opacity = 1
			self.label_top.disabled= False
if __name__ =='__main__':
	App().run()