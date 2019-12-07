from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
Builder.load_file('KV/tri.kv')
class Try(BoxLayout):
    def __init__(self, **kwargs):
        super(Try, self).__init__(**kwargs)
        self.ids.cb_chronic_cough.active = True

    # def fun(self):
    #     print(self.ids.cb_chronic_cough.active)
    pass


class Main2(App):
    def build(self):
        return Try()

Main2().run()