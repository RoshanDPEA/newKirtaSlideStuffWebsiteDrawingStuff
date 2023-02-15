from kivy.app import App
from kivymd.tools.hotreload.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

#code for multiple windows https://www.techwithtim.net/tutorials/kivy-tutorial/multiple-screens/

Builder.load("kivyStuff.kv")

"""
class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
"""




# copy the root widget in the other screen with differnt images
class MainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)


class Window1(FloatLayout):
    def __init__(self, **kwargs):
        super(Window1, self).__init__(**kwargs)




class WindowManager(ScreenManager):
    def get_classes(self):
        return {screen.__class__.__name__: screen.__class__.__module__ for screen in self.screens}

kv = Builder.load_file("my.kv")


class MyMainApp(App):
    DEBUG = True
    sm = None
    state = {}

    def build_app(self, first=False):
        if self.sm is None:
            self.state = {'current': 'one',
                          'MainWindow': 'data one',
                          'Window1': 'data two'}
        else:
            self.state = {'current': self.sm.current,
                          'MainWindow': self.sm.get_screen('MainWindow').ids.data.text,
                          'Window1': self.sm.get_screen('Window1').ids.data.text}

        KV_FILES = []
        self.sm = WindowManager()
        CLASSES = self.sm.get_classes()

    def apply_state(self, state):
        self.sm.current = state['current']
        self.sm.get_screen('one').ids.data.text = state['one']
        self.sm.get_screen('two').ids.data.text = state['two']

        return self.sm
    

if __name__ == "__main__":
    MyMainApp().run()
