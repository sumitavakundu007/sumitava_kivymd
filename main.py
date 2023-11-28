import json
import numpy as np
import kivy
from kivy.app import App
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivymd.uix.textfield import MDTextField
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDFloatingActionButton, MDRectangleFlatButton

class MyStoreApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.material_style = "M3"
        self.key_input = MDTextField()
        self.value_input = MDTextField()
        self.save_button = MDTextField()
        self.save_button = MDRectangleFlatButton()
        self.search_input = MDTextField()
        self.go_button = MDRectangleFlatButton()
        self.clear_button = MDRectangleFlatButton()

    def build(self):
        fab = MDFloatingActionButton(icon="pencil")
        fab.pos_hint = {"center_x": .45, "center_y": .9}

        get_fab = MDFloatingActionButton(icon="android")
        get_fab.pos_hint = {"center_x": .55, "center_y": .9}

        self.layout = MDRelativeLayout()
        self.layout.add_widget(fab)
        self.layout.add_widget(get_fab)
        fab.bind(on_release=self.update_data)
        get_fab.bind(on_release=self.search_data)
        return self.layout

    def search_data(self, instance):
        # REmove some widgets
        self.layout.remove_widget(self.key_input)
        self.layout.remove_widget(self.value_input)
        self.layout.remove_widget(self.save_button)

        # Create a text input for the name
        self.search_input = MDTextField(hint_text="Enter your search", mode="rectangle")
        self.layout.add_widget(self.search_input)
        self.search_input.pos_hint = {"center_x": 0.5, "center_y": 0.7}
        self.search_input.size_hint_x = 0.5

        # Create a button to go the data
        self.go_button = MDRectangleFlatButton(text='Go', theme_text_color='Custom', text_color="black", line_color='white')
        self.go_button.bind(on_release=self.get_data)
        self.layout.add_widget(self.go_button)
        self.go_button.pos_hint = {"center_x": .8, "center_y": .7}
        self.go_button.size_hint_x = 0.1

        # Create a button to clear the data
        self.clear_button = MDRectangleFlatButton(text='Clear', theme_text_color='Custom', text_color="black", line_color='red')
        self.clear_button.bind(on_release=self.clear_data)
        self.layout.add_widget(self.clear_button)
        self.clear_button.pos_hint = {"center_x": .5, "center_y": .3}
        self.clear_button.size_hint_x = 0.1

    def get_data(self, instance):
        search_key = self.search_input.text

        with open('my_data.json') as f:
            data = json.load(f)

        search_value = data[search_key]
        self.search_label = MDLabel(text=search_value)
        self.layout.add_widget(self.search_label)
        self.search_label.pos_hint = {"center_x": .5, "center_y": .5}
        self.search_label.size_hint_x = 0.5

    def clear_data(self, instance):
        self.search_input.text = ''
        self.layout.remove_widget(self.search_label)

    def update_data(self, instance):
        # REmove some widgets
        self.layout.remove_widget(self.search_input)
        self.layout.remove_widget(self.go_button)
        self.layout.remove_widget(self.clear_button)

        # Create a text input for the name
        self.key_input = MDTextField(hint_text="Enter your key", mode="rectangle")
        self.layout.add_widget(self.key_input)
        self.key_input.pos_hint = {"center_x": 0.5, "center_y": 0.7}
        self.key_input.size_hint_x = 0.5


        # Create a text input for the value
        self.value_input = MDTextField(hint_text="Enter your value", mode="rectangle")
        self.layout.add_widget(self.value_input)
        self.value_input.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.value_input.size_hint_x = 0.5

        # Create a button to save the data
        self.save_button = MDRectangleFlatButton(text='Save', theme_text_color='Custom', text_color="black", line_color='red')
        self.save_button.bind(on_release=self.save_data)
        self.layout.add_widget(self.save_button)
        self.save_button.pos_hint = {"center_x": .5, "center_y": .3}
        self.save_button.size_hint_x = 0.1

    def save_data(self, instance):
        # Get the key and value from the text inputs
        key = self.key_input.text
        value = self.value_input.text

        with open('my_data.json') as f:
            data = json.load(f)

        data[key] = value
        with open('my_data.json', 'w') as g:
            json.dump(data, g, indent=4)

        # Clear the text inputs
        self.key_input.text = ''
        self.value_input.text = ''

if __name__ == '__main__':
    MyStoreApp().run()