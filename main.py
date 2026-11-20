
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.04, 0.03, 1)

class PrankApp(App):

    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="CYBER TERMINAL",
            font_size=28,
            color=(0, 1, 0.3, 1)
        )

        message = Label(
            text="SYSTEM READY",
            font_size=20,
            color=(0, 1, 0.3, 1)
        )

        button = Button(
            text="START PRANK",
            font_size=22
        )

        def prank(instance):
            message.text = (
                "ACCESS GRANTED!\n\n"
                "YOU GOT PRANKED 😂\n\n"
                "JUST A JOKE!"
            )

        button.bind(on_press=prank)

        layout.add_widget(title)
        layout.add_widget(message)
        layout.add_widget(button)

        return layout


PrankApp().run()
