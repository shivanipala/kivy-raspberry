from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()

msg['Subject'] = "Report"

# string to store the body of the mail
body = "Dear Sir/Ma'm,\nGreetins from DBreath Medical Devices LLP...\nThis email is sent to you from DBreath.Kindly note that an report is sent as an attachment to this mail. \nAll the best for your diagnosis. \nThank You, \nDBreath"

# attach the body with the msg instancevuyv
msg.attach(MIMEText(body, 'plain'))

filename = "inalreport1.pdf"
attachment = open( "C:\Kivy master\inalreport1.pdf", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

text = msg.as_string()

class widgets(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lbl = self.lbl = Label(text="Enter Your Email Id", pos=(330, 280), size=(150, 100), size_hint=(None, None),
                               halign='justify')
        btn1 = self.btn1 = Button(text="Send", pos=(320, 220), size=(80, 30), size_hint=(None, None))
        btn = self.btn = Button(text="Cancel", pos=(410, 220), size=(80, 30), size_hint=(None, None))
        ti = self.ti = TextInput(multiline=False, use_bubble=True, hint_text='example@gmail.com', pos=(310, 270),
                                 size=(200, 30),
                                 size_hint=(None, None))
        self.add_widget(lbl)
        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(ti)


def popup():
    widg = widgets()
    greet = Popup(title="Send Report To Email", content=widg, size=(290, 200), size_hint=(None, None),
                  auto_dismiss=False)
    greet.open()
    widg.btn.bind(on_press=lambda x: greet.dismiss())
    widg.btn1.bind(on_press=lambda b: send_email(text, widg.ti.text))


def send_email(text, mail_id):
    sender = "jamesshah@gecg28.ac.in"
    passwd = "vcygwfmsnzargutb"
    reciever = mail_id
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.ehlo()
    server.login(sender, passwd)
    server.sendmail(sender, reciever, text)
    print("Mail Sent Successfully!")


# mail = 'Body: "i m sending u the report."'


class ThisApp(App):

    def build(self):
        return popup()
