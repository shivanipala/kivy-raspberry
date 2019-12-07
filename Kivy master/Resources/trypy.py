from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.graphics import Color

Window.clearcolor = (1, 1, 1, 1)




Builder.load_file('main.kv')
Builder.load_file('screen1.kv')
# Builder.load_file('screen2.kv')
# class Try(BoxLayout):
#     def __init__(self, **kw):
#         super(Try, self).__init__(**kw)
#

class Screen1(Screen):

    def __init__(self, **kw):
        super(Screen1, self).__init__(**kw)
        print(self.ids.l1.text)

'''class Screen2(Screen):
    def __init__(self, **kw):
        super(Screen2, slef).__init__(**kw)
        print(self.ids.l2.text)
'''



class Main(App):
    def build(self):
        superbox= BoxLayout(orientation= "vertical")
        b1 = BoxLayout(orientation="vertical", size_hint=(1, .1))
        f1 = FloatLayout()
        #home button
        home_btn= Button(size_hint=(None,None), size=(50,50), background_color= [255,255,255,0], pos= (7,430))
        home_img = Image(source= 'C:\Kivy master\Resources\home_btn.png', size=(50,50), pos= (7,430))
        home_btn.add_widget(home_img)

        #exit btn
        exit_btn=Button(size_hint=(None,None), size=(50,50), background_color= [255,255,255,0], pos= (760,430))
        exit_img = Image(source='C:\Kivy master\Resources\exit_btn.png', size=(30, 30), pos=(760, 430))
        exit_btn.add_widget(exit_img)

        #labels of patient id and name
        id_btn= Label(markup= True, text= "[color=#000000][font=OpenSans]Patient id:[/color][/font]", size_hint= (None,None), pos= (55,415))
        name_btn= Label(markup= True, text= "[color=#000000][font=OpenSans]Name:[/color][/font]", size_hint= (None,None), pos= (43,395))
        idvalue_btn= Label(markup= True, text= "[color=#000000][font=OpenSans]204[/color][/font]", size_hint= (None,None), pos= (120,415))
        namevalue_btn= Label(markup= True, text= "[color=#000000][font=OpenSans]Khushi Shah[/color][/font]", size_hint= (None,None), pos= (115, 395))

        f1.add_widget(home_btn)
        f1.add_widget(exit_btn)
        f1.add_widget(id_btn)
        f1.add_widget(name_btn)
        f1.add_widget(idvalue_btn)
        f1.add_widget(namevalue_btn)
        b1.add_widget(f1)

        superbox.add_widget(b1)


        b2 = BoxLayout(orientation="vertical", size_hint=(1, .8))
        b2.canvas.add(Color(0,0,0,0.3))
        b2.canvas.add( Rectangle (size= (800,7), pos=(0,420)))
        b2.canvas.add( Rectangle (size= (800,7), pos=(0,45)))
        sm = ScreenManager()
        # self.add_widget(sm)
        sm.add_widget(Screen1(name="Screen1"))
        superbox.add_widget(b2)
        # self.add_widget(b2)
        b2.add_widget(sm)

        b3 = BoxLayout(orientation="vertical", size_hint=(1, .1))
        f3= FloatLayout()
        contact_lbl= Label(markup= True, text= "[font=OpenSans][color=#000000][u]Contact us[/ref][/u][/color][/font]",  size_hint= (None,None), size= (50,50), pos= (365,-5))
        back_btn= Button(size_hint= (None,None), size= (50,50),background_color= [255,255,255,0], pos= (10,5))
        back_img= Image(source= 'C:\Kivy master\Resources\s_back.png', size=(40, 40), pos=(10,5))
        back_btn.add_widget(back_img)
        f3.add_widget(back_btn)
        f3.add_widget(contact_lbl)

        b3.add_widget(f3)
        superbox.add_widget(b3)
        return superbox

Main().run()