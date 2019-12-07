import mysql.connector
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.graphics import Color
import cnumpy
import spidev
import report
import form
import my_fn
import time
import math
from pre_graph import *
from functools import partial
import report
import form

Window.clearcolor = (1, 1, 1, 1)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

Config.set('kivy', 'keyboard_mode', 'systemanddocked')
from os import listdir
kv_path = './KV/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

mydb = mysql.connector.connect(host="localhost", user="newuser", passwd="password", database="db1")
mycursor = mydb.cursor()

global list
list= []

class AdminLoginScreen(Screen):
    def admin_login(self):
        if self.ids.admin_un.text == 'admin' and self.ids.admin_pw.text == 'admin':
            screen_mgr.current = 'AdminMain_Screen'
            self.ids.admin_un.text = ''
            self.ids.admin_pw.text = ''
            print(self)
        else:
            Popup(title="Invalid Details", title_align="center",
                  content=Label(text="Invalid Username/Password."),
                  size=(300, 200),
                  size_hint=(None, None), auto_dismiss=True).open()
            self.ids.admin_un.text = ''
            self.ids.admin_pw.text = ''

class AdminMainScreen(Screen):
    def admin_logout(self):
        screen_mgr.current = "AdminLogin_Screen"

class AlreadyRegisteredScreen(Screen):
    def __init__(self, **kw):
        super(AlreadyRegisteredScreen, self).__init__(**kw)
        self.ids.search_btn.bind(on_press=lambda x: self.prints())
        self.ids.p_id.color = (0, 0, 0, 1)
        self.ids.p_id.bold = True
        self.ids.p1_name.markup = True
        self.ids.p_id.font = "OpenSans"
        self.ids.p1_id.color = (0, 0, 0, 1)
        self.ids.p1_name.color = (0, 0, 0, 1)
        self.ids.p1_gender.color = (0, 0, 0, 1)
        self.ids.p2_id.color = (0, 0, 0, 1)
        self.ids.p2_name.color = (0, 0, 0, 1)
        self.ids.p2_gender.color = (0, 0, 0, 1)
        self.ids.p3_id.color = (0, 0, 0, 1)
        self.ids.p3_name.color = (0, 0, 0, 1)
        self.ids.p3_gender.color = (0, 0, 0, 1)

    def prints(self):
        my_fn.fetch_info(self, self.ids.pa_fname.text, self.ids.pa_lname.text, self.ids.pa_id.text)

    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class CongratsScreen(Screen, Image):
    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class ContactScreen(Screen):
    def binds(self):
        self.ids.home.bind(on_press= partial(next, sm.current, "Home_Screen"))
    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class DiagnosisScreen(Screen):
    def __init__(self, **kwargs):
        super(DiagnosisScreen, self).__init__(**kwargs)

class DrugNamesScreen(Screen):
    list= {'shivani', 'harshal', 'neha', 'mahek', 'vishw'}
    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class FormScreen(Screen):
    yes = ObjectProperty(True)
    no = ObjectProperty(True)

    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

    def submit_popup(self):
        print(self.ids.p_lname.text)
        p_weight = self.ids.p_weight
        p_height = self.ids.p_height
        p_smoke_yes = self.ids.p_smoke_yes
        p_smoke_no = self.ids.p_smoke_no
        p_gender_m = self.ids.p_gender_m
        p_gender_f = self.ids.p_gender_f
        p_gender_o = self.ids.p_gender_o
        p_fname = self.ids.p_fname
        p_mname = self.ids.p_mname
        p_lname = self.ids.p_lname
        p_dob = self.ids.p_dob
        p_age = self.ids.p_age

        form.submit_popup(p_weight, p_height, p_smoke_yes, p_smoke_no, p_dob, p_age,
                          p_fname, p_gender_f,
                          p_gender_m,
                          p_gender_o,
                          p_lname, p_mname)
    def __init__(self, **kw):
        super(FormScreen, self).__init__(**kw)
        self.ids["p_id"].color = (0, 0, 1, 1)
        self.ids["p_id"].text = my_fn.count_pid()
    #
    # def __init__(self, **kw):
    #     super().__init__(**kw)

        # self.ids["p_id"].color = (0, 0, 1, 1)
        # self.ids["p_id"].text = my_fn.count_pid()
        # p_fname = self.ids.p_fname.text
        # p_lname = self.ids.p_mname.text
        # p_id = self.ids.p_lname.text
        # self.ids.p_dob.bind(on_text_validate=lambda x: match(self.ids.p_dob.text, self.ids.p_age.text ))

    # self.ids.submit_btn.on_press = partial(my_fn.match, self.ids.p_dob.text, self.ids.p_age.text)
    # self.ids.submit_btn.on_press = my_fn.fun(p_fname.text, p_mname.text, p_lname.text, p_height.text, p_weight.text,
    #                                          p_dob.text)

def showKeyboard(self):
    keyboard = VKeyboard()
    return keyboard

class FVCScreen(Screen):
    def binds(self):
        self.ids.pre_broncholidator_test.bind(on_press= partial(next, sm.current, "Pre_Test_Screen"))
        self.ids.post_broncholidator_test.bind(on_press=partial(next, sm.current, "Post_Test_Screen"))

    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class HomeScreen(Screen):
    def __init__(self, **kw):
        super(HomeScreen, self).__init__(**kw)

    def binds(self):
        self.ids.medical_questionnare.bind(on_press= partial(next, sm.current, "Question_Screen"))
        self.ids.test.bind(on_press= partial(next, sm.current, "Test_Screen"))
        self.ids.diagnosis.bind(on_press=partial(next, sm.current, "Diagnosis_Screen"))
        # self.ids.diagnosis.bind(on_press=partial(DiagnosisScreen.verify))
        self.ids.manual.bind(on_press=partial(next, sm.current, "Congrats_Screen"))
        self.ids.treatment.bind(on_press=partial(next, sm.current, "Treatment_Screen"))
        self.ids.manual.bind(on_press=partial(next, sm.current, "Congrats_Screen"))
        self.ids.life_with_copd.bind(on_press=partial(next, sm.current, "LifeWithCopd_Screen"))



    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class LifeWithCopdScreen(Screen):
    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class PostTestScreen(Screen):
    post_click = 0
    def post_change_screen(self):
        self.post_click += 1
        if self.post_click == 6:
            next(sm.current, "Test_Result_Screen")
            self.post_click = 0

    def calculate_average(self):
        from pre_graph import post_fev1_avg, post_fvc_avg, post_fev1_fvc_avg, post_pef_avg, post_fef25_avg, \
            post_fef_50_75_avg
        global post_fev1_avg, post_fvc_avg, post_fev1_fvc_avg, post_fet_avg, post_pef_avg, post_fef25_avg \
            , post_fef_50_75_avg
        post_fev1_avg = post_fev1_avg / 6
        post_fvc_avg = post_fvc_avg / 6
        post_fev1_fvc_avg = post_fev1_fvc_avg / 6
        post_fet_avg = t
        post_pef_avg = post_pef_avg / 6
        post_fef25_avg = post_fef25_avg / 6
        post_fef_50_75_avg = post_fef_50_75_avg / 6

    def start(self):
        start_post(self)

    def VOlume_graph(self):
        volume_graph_post(self)

    def submit(self):
        submit_post(self)

    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class PreTestScreen(Screen):
    pre_click = 0
    def pre_change_screen(self):
        self.pre_click += 1
        if self.pre_click == 6:
            next(sm.current, "Post_Test_Screen")
            self.pre_click = 0

    def calculate_average(self):
        from pre_graph import pr_fev1_avg, pr_fvc_avg, pr_fev1_fvc_avg, pr_pef_avg, pr_fef25_avg, pr_fef_50_75_avg
        global pr_fev1_avg, pr_fvc_avg, pr_fev1_fvc_avg, pr_fet_avg, pr_pef_avg, pr_fef25_avg, pr_fef_50_75_avg
        pr_fev1_avg = pr_fev1_avg / 6
        pr_fvc_avg = pr_fvc_avg / 6
        pr_fev1_fvc_avg = pr_fev1_fvc_avg / 6
        pr_fet_avg = t
        pr_pef_avg = pr_pef_avg / 6
        pr_fef25_avg = pr_fef25_avg / 6
        pr_fef_50_75_avg = pr_fef_50_75_avg / 6

    def __init__(self, **kw):
        super(PreTestScreen, self).__init__(**kw)
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.plot1 = MeshLinePlot(color=[1, 0, 0, 1])

    def start(self):
        # pre_graph.start(self)
        start(self)

    def VOlume_graph(self):
        volume_graph(self)

    def submit(self):
        submit(self)

    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

# Post Results Screen inside Test Result Screen
class Post_Result(Screen):
    def print_fev1(self):
        global post_fev1_avg
        print(post_fev1_avg)
        return str(post_fev1_avg)

    def print_fvc(self):
        global post_fvc_avg
        print(post_fvc_avg)
        return str(post_fvc_avg)

    def print_fev1_fvc(self):
        global pr_fev1_fvc_avg
        print(pr_fev1_fvc_avg)
        return str(post_fev1_fvc_avg)

    def print_fet(self):
        global pr_fet_avg
        print(pr_fet_avg)
        return str(post_fet_avg)

    def print_pef(self):
        global pr_pef_avg
        print(pr_pef_avg)
        return str(post_pef_avg)

    def print_fef25(self):
        global pr_fef25_avg
        print(pr_fef25_avg)
        return str(post_fef25_avg)

    def print_fef50_75(self):
        global pr_fef_50_75_avg
        print(pr_fef_50_75_avg)
        return str(post_fef_50_75_avg)

# Pre Results Screen inside Test Result Screen
class Pre_Result(Screen):
    print
    'pre_result running'
    global pr_fev1_avg, pr_fvc_avg, pr_fev1_fvc_avg, pr_fet_avg, pr_pef_avg, pr_fef25_avg, pr_fef_50_75_avg

    # print ('check this22', pr_fev1_avg, pr_fvc_avg)
    # def __init__(self, **kw):
    # super(Pre_Result, self).__init__(**kw)
    # self.ids.tr_pr_fvc.text = self.print_pef()
    def print_fev1(self):
        global pr_fev1_avg
        print(pr_fev1_avg)
        return str(pr_fev1_avg)

    def print_fvc(self):
        global pr_fvc_avg
        print(pr_fvc_avg)
        return str(pr_fvc_avg)

    def print_fev1_fvc(self):
        global pr_fev1_fvc_avg
        print(pr_fev1_fvc_avg)
        return str(pr_fev1_fvc_avg)

    def print_fet(self):
        global pr_fet_avg
        print(pr_fet_avg)
        return str(pr_fet_avg)

    def print_pef(self):
        global pr_pef_avg
        print(pr_pef_avg)
        return str(pr_pef_avg)

    def print_fef25(self):
        global pr_fef25_avg
        print(pr_fef25_avg)
        return str(pr_fef25_avg)

    def print_fef50_75(self):
        global pr_fef_50_75_avg
        print(pr_fef_50_75_avg)
        return str(pr_fef_50_75_avg)

class PulseOximetryScreen(Screen):
    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class QuestionScreen(Screen):
    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()
    def binds(self):
        self.ids.next.bind(on_press= partial(next, sm.current, "YesNoQuestion_Screen"))
    def edit(self):
        self.ids.cb_dyspnea.disabled = False
        self.ids.cb_sputum.disabled = False
        self.ids.cb_cough.disabled = False
        self.ids.cb_wheezing.disabled = False
        self.ids.cb_yes.disabled = False
        self.ids.cb_no.disabled = False

    def submit(self):
        global dyspnea
        self.ids.cb_dyspnea.disabled = True
        self.ids.cb_sputum.disabled = True
        self.ids.cb_cough.disabled = True
        self.ids.cb_wheezing.disabled = True
        self.ids.cb_yes.disabled = True
        self.ids.cb_no.disabled = True
        dyspnea = self.ids.cb_dyspnea.active

class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super(RegistrationScreen, self).__init__(**kwargs)
    def binds(self, *args):

        self.ids.new_registration.bind(on_press=partial(next, sm.current, "Form_Screen"))
        self.ids.already_registered.bind(on_press= partial(next, sm.current, "AlreadyRegistered_Screen"))

    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class SVCScreen(Screen):
    def binds(self):
        self.ids.start.bind(on_press=partial(next, sm.current, "SVC1_Screen"))

    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class SVC1Screen(Screen):
    def binds(self):
        self.ids.info.bind(on_press=partial(next, sm.current, "SVCInfo_Screen"))
    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class SVCInfoScreen(Screen):
    def binds(self):
        self.ids.next.bind(on_press=partial(next, sm.current, "SVC2Info_Screen"))

    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class SVC2InfoScreen(Screen):
    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class TestScreen(Screen):
    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

    def binds(self):
        self.ids.FVC.bind(on_press=partial(next, sm.current, "FVC_Screen"))
        self.ids.SVC.bind(on_press=partial(next, sm.current, "SVC_Screen"))
        self.ids.pulse_oximetry.bind(on_press=partial(next, sm.current, "PulseOximetry_Screen"))

class TestResultScreen(Screen):
    def __init__(self, **kw):
        super(TestResultScreen, self).__init__(**kw)
        pre_result = Pre_Result()
        self.ids.pre_btn.on_press = partial(pre_result.try_fn)

    def mail_popup(self):
        report.popup()

    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

class TreatmentScreen(Screen):
    trt_list = ['oxygen_therapy', 'vaccination', 'bronchodilator', 'pulmonary_rehabilitation', 'smoking_cessation']

    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

    def binds(self):
        self.ids.vaccine.bind(on_press=partial(next, sm.current, "Vaccination_Screen"))
        self.ids.drugs.bind(on_press=partial(next, sm.current, "DrugNames_Screen"))

class YesNoQuestionScreen(Screen):
    def __init__(self, **kw):
        super(YesNoQuestionScreen, self).__init__(**kw)
        # global dyspnea
        # self.id['cb_dyspnea'].active =True
            # dyspnea = True
    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()

    def submit(self):
        self.ids.cb1_no.disabled = True
        self.ids.cb1_yes.disabled = True
        self.ids.cb2_no.disabled = True
        self.ids.cb2_yes.disabled = True
        self.ids.cb3_no.disabled = True
        self.ids.cb3_yes.disabled = True
        self.ids.cb4_no.disabled = True
        self.ids.cb4_yes.disabled = True
        self.ids.cb5_no.disabled = True
        self.ids.cb5_yes.disabled = True
        self.ids.cb6_no.disabled = True
        self.ids.cb6_yes.disabled = True
        self.ids.cb7_no.disabled = True
        self.ids.cb7_yes.disabled = True

    def edit(self):
        self.ids.cb1_no.disabled = False
        self.ids.cb1_yes.disabled = False
        self.ids.cb2_no.disabled = False
        self.ids.cb2_yes.disabled = False
        self.ids.cb3_no.disabled = False
        self.ids.cb3_yes.disabled = False
        self.ids.cb4_no.disabled = False
        self.ids.cb4_yes.disabled = False
        self.ids.cb5_no.disabled = False
        self.ids.cb5_yes.disabled = False
        self.ids.cb6_no.disabled = False
        self.ids.cb6_yes.disabled = False
        self.ids.cb7_no.disabled = False
        self.ids.cb7_yes.disabled = False

class VaccinationScreen(Screen):
    def exit_prog(self):
        App.get_running_app().stop()
        Window.close()


def next(this_screen, next_screen, *args):
    global list
    list.append(this_screen)
    sm.current = next_screen

def back(*args):
    global list
    if list:
        sm.current = list.pop()
    return False

def exit_prog(*args):
    App.get_running_app().stop()
    Window.close()

sm = ScreenManager()
sm.add_widget(RegistrationScreen(name="Registration_Screen"))
sm.add_widget(FormScreen(name="Form_Screen"))
sm.add_widget(HomeScreen(name="Home_Screen"))
sm.add_widget(AlreadyRegisteredScreen(name="AlreadyRegistered_Screen"))
sm.add_widget(LifeWithCopdScreen(name="LifeWithCopd_Screen"))
sm.add_widget(FVCScreen(name="FVC_Screen"))
sm.add_widget(TestScreen(name="Test_Screen"))
sm.add_widget(PreTestScreen(name="Pre_Test_Screen"))
sm.add_widget(PostTestScreen(name="Post_Test_Screen"))
sm.add_widget(TestResultScreen(name="Test_Result_Screen"))
sm.add_widget(CongratsScreen(name="Congrats_Screen"))
sm.add_widget(QuestionScreen(name="Question_Screen"))
sm.add_widget(YesNoQuestionScreen(name="YesNoQuestion_Screen"))
sm.add_widget(ContactScreen(name="Contact_Screen"))
sm.add_widget(TreatmentScreen(name="Treatment_Screen"))
sm.add_widget(DiagnosisScreen(name="Diagnosis_Screen"))
sm.add_widget(SVCScreen(name="SVC_Screen"))
sm.add_widget(SVC1Screen(name="SVC1_Screen"))
sm.add_widget(SVCInfoScreen(name="SVCInfo_Screen"))
sm.add_widget(SVC2InfoScreen(name="SVC2Info_Screen"))
sm.add_widget(PulseOximetryScreen(name="PulseOximetry_Screen"))
sm.add_widget(VaccinationScreen(name="Vaccination_Screen"))
sm.add_widget(DrugNamesScreen(name= "DrugNames_Screen"))
sm.add_widget(AdminLoginScreen(name="AdminLogin_Screen"))
sm.add_widget(AdminMainScreen(name="AdminMain_Screen"))

#Superbox
superbox = BoxLayout(orientation="vertical")
# header declaration
b1 = BoxLayout(orientation="vertical", size_hint=(1, .1))
f1 = FloatLayout()
#header home button
home_btn = Button(size_hint=(None, None), size=(50, 50), background_color=[255, 255, 255, 0], pos=(7, 420))
home_btn.bind(on_press= partial(next, sm.current, "Home_Screen"))
home_img = Image(source='C:\Kivy master\Resources\home_btn.png', size=(50, 50), pos=(7, 430))
home_btn.add_widget(home_img)
#header exit btn
exit_btn = Button(size_hint=(None, None), size=(50, 50), background_color=[255, 255, 255, 0], pos=(760, 430))
exit_img = Image(source='C:\Kivy master\Resources\exit_btn.png', size=(30, 30), pos=(760, 430))
exit_btn.add_widget(exit_img)
exit_btn.bind(on_press= partial(exit_prog))
#header labels of patient id and name
id_btn = Label(markup=True, text="[color=#000000][font=OpenSans]Patient id:[/color][/font]",
               size_hint=(None, None), pos=(55, 415))
name_btn = Label(markup=True, text="[color=#000000][font=OpenSans]Name:[/color][/font]", size_hint=(None, None),
                 pos=(43, 395))
idvalue_btn = Label(markup=True, text="[color=#000000][font=OpenSans]204[/color][/font]",
                    size_hint=(None, None), pos=(120, 415))
namevalue_btn = Label(markup=True, text="[color=#000000][font=OpenSans]Khushi Shah[/color][/font]",
                      size_hint=(None, None), pos=(115, 395))
#adding header widgets
f1.add_widget(home_btn)
f1.add_widget(exit_btn)
f1.add_widget(id_btn)
f1.add_widget(name_btn)
f1.add_widget(idvalue_btn)
f1.add_widget(namevalue_btn)
b1.add_widget(f1)
superbox.add_widget(b1)

# adding screenmanager widget
b2 = BoxLayout(orientation="vertical", size_hint=(1, .8))
b2.canvas.add(Color(0, 0, 0, 0.3))
b2.canvas.add(Rectangle(size=(800, 7), pos=(0, 420)))
b2.canvas.add(Rectangle(size=(800, 7), pos=(0, 45)))
b2.add_widget(sm)
superbox.add_widget(b2)

# footer declaration
b3 = BoxLayout(orientation="vertical", size_hint=(1, .1))
f3 = FloatLayout()
contact_lbl = Label(markup=True, text="[font=OpenSans][color=#000000][ref=some][u]Contact us[/u][/ref][/color][/font]",
                    size_hint=(None, None), size=(50, 50), pos=(365, -5))
contact_lbl.on_ref_press= partial(next, sm.current, "Contact_Screen")
back_btn = Button(size_hint=(None, None), size=(50, 50), background_color=[255, 255, 255, 0], pos=(10, 5))
back_img = Image(source='C:\Kivy master\Resources\s_back.png', size=(40, 40), pos=(10, 5))
back_btn.bind(on_press= partial(back))
back_btn.add_widget(back_img)
f3.add_widget(back_btn)
f3.add_widget(contact_lbl)
b3.add_widget(f3)
superbox.add_widget(b3)

class ThisApp(App):
    def __init__(self, **kw):
        super(ThisApp, self).__init__(**kw)
        self.list = []
        dyspnea = True
    def build(self):
        return superbox
if __name__ == '__main__':
    ThisApp().run()
