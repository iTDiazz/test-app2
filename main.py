from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
class MainApp(MDApp):
    def build(self):
        def press_button(self):
            if self.icon == "android":
                self.icon = "microsoft-windows"
            else:
                self.icon = "android"

        button = MDIconButton(icon="android",
                              on_release=press_button)

        return button

MainApp().run()
