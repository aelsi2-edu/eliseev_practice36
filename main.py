from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.config import Config
from kivy.graphics import Color, Ellipse, Line

def HSVtoRGB(color1,color2,color3):
    return Color(color1, color2, color3, mode='hsv').rgba

class BrushPreview(Widget):
    pass

class PaintArea(Widget):
    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return
        with self.canvas:
            Color(*self.color)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.thickness)
    def on_touch_move(self, touch):
        if not self.collide_point(*touch.pos):
            return
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]
    def clear(self):
        self.canvas.clear()

class PaintApp(App):
    def on_hue_change(self, value):
        color = HSVtoRGB(value, 1, 1)
        self.root.ids.painter.color = color
        self.root.ids.preview.color = color
    def on_thickness_change(self, value):
        self.root.ids.painter.thickness = value
        self.root.ids.preview.thickness = value
    def clear_click(self):
        self.root.ids.painter.clear()


if __name__ == '__main__':
    Config.set('graphics', 'resizable', '0')
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '640')
    PaintApp().run()