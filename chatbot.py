import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


def get_plant_info(plant_name):
    # Bitki bilgilerini API den çeker
    base_url = 'https://openfarm.cc/api/v1/crops'
    try:
        response = requests.get(base_url, params={'filter': plant_name}, timeout=10)
    except requests.RequestException:
        return "Plant service is temporarily unavailable."
    if response.status_code == 200:
        try:
            data = response.json()
        except ValueError:
            return "Plant service returned an invalid response."
        if data['data']:
            plant = data['data'][0]['attributes']
            name = plant.get('name', 'Unknown')
            description = plant.get('description', 'No information available')
            sun_requirements = plant.get('sun_requirements', 'No information available')
            sowing_method = plant.get('sowing_method', 'No information available')
            spread = plant.get('spread', 'No information available')
            row_spacing = plant.get('row_spacing', 'No information available')
            return (f"Name: {name}\n\n"
                    f"Description: {description}\n\n"
                    f"Sun Requirements: {sun_requirements}\n\n"
                    f"Sowing Method: {sowing_method}\n\n"
                    f"Spread: {spread}\n\n"
                    f"Row Spacing: {row_spacing}")
        else:
            return "Plant information not found."
    else:
        return "API access error."

class FarmingChatbot(App):
    def build(self):
        # Chatbot Arayüz
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="Enter the name of the vegetable (e.g., Potato):", font_size='20sp')
        self.layout.add_widget(self.label)

        self.input = TextInput(multiline=False, font_size='18sp', size_hint_y=None, height=40)
        self.layout.add_widget(self.input)

        self.button = Button(text="Get Information", size_hint_y=None, height=50, font_size='18sp')
        self.button.bind(on_press=self.get_info)
        self.layout.add_widget(self.button)

        self.scrollview = ScrollView(size_hint=(1, 1))
        self.result = Label(text="", font_size='16sp', size_hint_y=None, markup=True)
        self.result.bind(texture_size=self.result.setter('size'))
        self.scrollview.add_widget(self.result)
        self.layout.add_widget(self.scrollview)

        return self.layout

    def get_info(self, instance):
        # Kullanıcının girdiği bitki ismi alınır ve bilgiler get_plant_info fonksiyonuyla alınır
        plant_name = self.input.text.strip().lower()
        if not plant_name:
            self.result.text = "Please enter a plant name."
            return
        self.result.text = "Loading information..."
        info = get_plant_info(plant_name)
        self.result.text_size = (self.scrollview.width, None)  # Metin için genişlik ayarı
        self.result.text = info

if __name__ == "__main__":
    FarmingChatbot().run()
