from kivy.app import App
from kivy.uix.label import Label
import datetime    
from kivy.uix.image import AsyncImage 
from kivy.uix.floatlayout import FloatLayout # import FloatLayout  

def daycount():
        today = datetime.datetime.now()
        NewYear = datetime.datetime(year=2021,month=1,day=1)
        days = (NewYear - today).days
        print(days)
        text = str(days)
        return text

class MainApp(App):  

    def build(self):
        Layout = FloatLayout(size = (300,300)) 
        label = Label(text= daycount()+' days left in New Year 2021!!!',
                      size_hint=(1, 1),
                      pos_hint={'center_x': .5, 'center_y': .5})
        Layout.add_widget(label)
        return Layout

if __name__ == '__main__':
    app = MainApp()
    app.run()