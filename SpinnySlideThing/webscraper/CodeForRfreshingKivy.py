#https://dev.to/jennasys/setting-up-hot-reload-with-kivymd-42h5

class MainApp(MDApp):  
    DEBUG = True  
    sm = None  

    def build_app(self, first=False):  
        if self.sm is None:  
            self.state = {'current': 'one',  
                          'one': 'data one',  
                          'two': 'data two'}  
        else:  
            self.state = {'current': self.sm.current,  
                          'one': self.sm.get_screen('one').ids.data.text,  
                          'two': self.sm.get_screen('two').ids.data.text}  

        KV_FILES = []  
        self.sm = SM()  
        CLASSES = self.sm.get_classes()  

        return self.sm  

    def apply_state(self, state):  
        self.sm.current = state['current']  
        self.sm.get_screen('one').ids.data.text = state['one']  
        self.sm.get_screen('two').ids.data.text = state['two']
