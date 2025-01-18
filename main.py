from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout

# Dict of cities - {city : lat, lng}
from data import CITIES

from api import response_fuel_price

class FuelPriceAPP(App):
    def build(self):

        # main layout for app
        self.layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )

        # label for messages and results
        self.label = Label(text='Виберіть місто')
        self.layout.add_widget(self.label)

        # spinner for select a city
        self.spinner = Spinner(
            text='Виберіть місто',
            values=list(CITIES.keys()),
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.spinner)

        # button for get fuel prices
        self.button = Button(text='Дізнатися ціни', size_hint=(1, 0.2))
        self.button.bind(on_press=self.get_data)
        self.label.add_widget(self.button)

        return self.layout

    def get_data(self, instance):
        response_fuel_price(self.spinner.text, self.label)

if __name__ == '__main__':
    FuelPriceAPP().run()
