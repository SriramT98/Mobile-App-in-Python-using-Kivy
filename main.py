import kivy
from kivy.app import App  #import App module
from kivy.uix.gridlayout import GridLayout #For creating grid
from kivy.uix.label import Label #For creating labels
from kivy.uix.textinput import TextInput #To take input
from kivy.uix.bubble import Button #For creating a button

class childApp(GridLayout):
    def __init__(self,**Kwargs):
        super(childApp,self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Student name'))
        self.S_name =TextInput()
        self.add_widget(self.S_name)

        self.add_widget(Label(text='Student marks'))
        self.S_marks = TextInput()
        self.add_widget(self.S_marks)

        self.add_widget(Label(text='Student gender'))
        self.S_gender = TextInput()
        self.add_widget(self.S_gender)

        self.press =Button(text='Click me')
        self.press.bind(on_press= self.click_me)
        self.add_widget(self.press)

    def click_me(self,instance):
        print("Name of the student is "+ self.S_name.text)
        print("Marks of the student is " + self.S_marks.text)
        print("Gender of the student is " + self.S_gender.text)
        print(" ")

class parentApp(App):
    def build(self):
        return childApp()

if __name__=="__main__":
    parentApp().run()
