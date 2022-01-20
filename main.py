from kivymd.app import MDApp
from kivy_garden.mapview import MapMarkerPopup


class MainApp(MDApp):
    def on_start(self):
        marker = MapMarkerPopup(lat=10.1, lon=10.4, source='marker.png')
        self.root.add_widget(marker)
        pass


MainApp().run()