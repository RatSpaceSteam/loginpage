from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file("LoginPage.kv")

class LoginPageApp(App):
    def build(self):
        return LoginPageManager()

class LoginPageManager(ScreenManager):
    pass

class BoxLayoutExample(BoxLayout):
    pass
class Question1Screen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "error"

class Question2Screen(Screen):
    def answer_question(self, text):
        if text.lower() == "deep in the heart of texas.":
            self.ids.test.text = "CORRECT"
            self.ids.test.font_size = 50
        else:
            self.ids.test.text = "WRONG"
            self.ids.test.font_size = 50

class CorrectScreen(Screen):
    def forward(self):
        self.manager.current = "question2"

class ErrorScreen(Screen):
    pass
if __name__ == "__main__":
    LoginPageApp().run()