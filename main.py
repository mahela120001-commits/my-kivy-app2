from kivy.app import App
from kivy.uix.button import Button

class AmarApp(App):
    def build(self):
        # এই বাটনটি আমাদের অ্যাপের স্ক্রিনে দেখাবে
        return Button(text="Ami Mobile diye App banachhi!")

if __name__ == "__main__":
    AmarApp().run()
