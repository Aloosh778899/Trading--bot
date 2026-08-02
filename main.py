from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class TradingBotApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.title_label = Label(text='Pocket Broker Trading Bot', font_size=22, size_hint_y=None, height=50)
        layout.add_widget(self.title_label)

        self.status_label = Label(text='الحالة: متوقف عن العمل', font_size=16, size_hint_y=None, height=40)
        layout.add_widget(self.status_label)

        self.pair_input = TextInput(text='EUR/CHF', multiline=False, size_hint_y=None, height=45)
        layout.add_widget(self.pair_input)

        self.start_btn = Button(text='تشغيل البوت', background_color=(0, 0.7, 0, 1), size_hint_y=None, height=55)
        self.start_btn.bind(on_press=self.start_bot)
        layout.add_widget(self.start_btn)

        self.stop_btn = Button(text='إيقاف البوت', background_color=(0.8, 0, 0, 1), size_hint_y=None, height=55)
        self.stop_btn.bind(on_press=self.stop_bot)
        layout.add_widget(self.stop_btn)

        return layout

    def start_bot(self, instance):
        pair = self.pair_input.text
        self.status_label.text = f'الحالة: جاري مراقبة زوج {pair}...'

    def stop_bot(self, instance):
        self.status_label.text = 'الحالة: تم إيقاف البوت.'

if __name__ == '__main__':
    TradingBotApp().run()
