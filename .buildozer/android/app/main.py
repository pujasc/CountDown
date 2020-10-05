from kivy.app import App
from kivy.uix.label import Label
import datetime    
from kivy.uix.image import AsyncImage 
from kivy.uix.floatlayout import FloatLayout # import FloatLayout  

from kivy.config import Config  
Config.set('graphics', 'resizable', True)

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
                      pos=(50,-250),
                      font_size='30sp')
        Layout.add_widget(label)
        
        Image = AsyncImage(source ='https://source.unsplash.com/random/?motivational',
                            pos=(0,100)) 
        Image.allow_stretch = True
        Image.keep_ratio = False
        Layout.add_widget(Image)
        return Layout

if __name__ == '__main__':
    app = MainApp()
    app.run()