import wx

from OpenGLCanvas import *


class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.radioButtonOrtho = wx.RadioButton(self, -1, pos=(820, 10))
        self.radioButtonOrtho.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.labelOrtho = wx.StaticText(self, -1, 'ortho', pos=(840, 10))
        self.labelOrtho.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.labelOrtho.SetForegroundColour('White')

        self.radioButtonFrust = wx.RadioButton(self, -1, pos=(820, 30))
        self.radioButtonFrust.SetValue(True)
        self.radioButtonFrust.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.labelFrust = wx.StaticText(self, -1, 'frust', pos=(840, 30))
        self.labelFrust.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.labelFrust.SetForegroundColour('White')

        self.rotXslider = wx.Slider(self, -1, pos=(820, 100), size=(140, 30),
                                    value=0, minValue=0, maxValue=360, style=wx.SL_HORIZONTAL)
        self.rotXlabel = wx.StaticText(self, -1, 'поворот вокруг Ox', pos=(840, 80))
        self.rotXlabel.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.rotXlabel.SetForegroundColour('RED')

        self.rotYslider = wx.Slider(self, -1, pos=(820, 150), size=(140, 30),
                                    value=0, minValue=0, maxValue=360, style=wx.SL_HORIZONTAL)
        self.rotYlabel = wx.StaticText(self, -1, 'поворот вокруг Oy', pos=(840, 130))
        self.rotYlabel.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.rotYlabel.SetForegroundColour('GREEN')

        self.rotZslider = wx.Slider(self, -1, pos=(820, 200), size=(140, 30),
                                    value=0, minValue=0, maxValue=360, style=wx.SL_HORIZONTAL)
        self.rotZlabel = wx.StaticText(self, -1, 'поворот вокруг Oz', pos=(840, 180))
        self.rotZlabel.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.rotZlabel.SetForegroundColour('BLUE')

        self.scaleXslider = wx.Slider(self, -1, pos=(820, 300), size=(140, 30),
                                      value=100, minValue=0, maxValue=200, style=wx.SL_HORIZONTAL)
        self.scaleXlabel = wx.StaticText(self, -1, 'масштабирование оси Ох', pos=(820, 280))
        self.scaleXlabel.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.scaleXlabel.SetForegroundColour('RED')

        self.scaleYslider = wx.Slider(self, -1, pos=(820, 350), size=(140, 30),
                                      value=100, minValue=0, maxValue=200, style=wx.SL_HORIZONTAL)
        self.scaleYlabel = wx.StaticText(self, -1, 'масштабирование оси Оу', pos=(820, 330))
        self.scaleYlabel.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.scaleYlabel.SetForegroundColour('GREEN')

        self.scaleZslider = wx.Slider(self, -1, pos=(820, 400), size=(140, 30),
                                      value=100, minValue=0, maxValue=200, style=wx.SL_HORIZONTAL)
        self.scaleZlabel = wx.StaticText(self, -1, 'масштабирование оси Оz', pos=(820, 380))
        self.scaleZlabel.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.scaleZlabel.SetForegroundColour('BLUE')

        self.shiftXslider = wx.Slider(self, -1, pos=(820, 500), size=(140, 30),
                                      value=0, minValue=-100, maxValue=100, style=wx.SL_HORIZONTAL)
        self.shiftXlabel = wx.StaticText(self, -1, 'сдвиг по оси Ох', pos=(845, 480))
        self.shiftXlabel.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.shiftXlabel.SetForegroundColour('RED')

        self.shiftYslider = wx.Slider(self, -1, pos=(820, 550), size=(140, 30),
                                      value=0, minValue=-100, maxValue=100, style=wx.SL_HORIZONTAL)
        self.shiftYlabel = wx.StaticText(self, -1, 'сдвиг по оси Оу', pos=(845, 530))
        self.shiftYlabel.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.shiftYlabel.SetForegroundColour('GREEN')

        self.shiftZslider = wx.Slider(self, -1, pos=(820, 600), size=(140, 30),
                                      value=0, minValue=-100, maxValue=100, style=wx.SL_HORIZONTAL)
        self.shiftZlabel = wx.StaticText(self, -1, 'сдвиг по оси Оz', pos=(845, 580))
        self.shiftZlabel.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.shiftZlabel.SetForegroundColour('BLUE')

        self.detailslider = wx.Slider(self, -1, pos=(820, 700), size=(140, 30),
                                      value=10, minValue=4, maxValue=25, style=wx.SL_HORIZONTAL)
        self.detailslabel = wx.StaticText(self, -1, 'детальность', pos=(855, 680))
        self.detailslabel.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.detailslabel.SetForegroundColour('White')

        self.canvas = OpenGlCanvas(self)

        self.Bind(wx.EVT_RADIOBUTTON, self.set_ortho, self.radioButtonOrtho)
        self.Bind(wx.EVT_RADIOBUTTON, self.set_frust, self.radioButtonFrust)

        self.Bind(wx.EVT_SLIDER, self.rotX, self.rotXslider)
        self.Bind(wx.EVT_SLIDER, self.rotY, self.rotYslider)
        self.Bind(wx.EVT_SLIDER, self.rotZ, self.rotZslider)

        self.Bind(wx.EVT_SLIDER, self.scaleX, self.scaleXslider)
        self.Bind(wx.EVT_SLIDER, self.scaleY, self.scaleYslider)
        self.Bind(wx.EVT_SLIDER, self.scaleZ, self.scaleZslider)

        self.Bind(wx.EVT_SLIDER, self.shiftX, self.shiftXslider)
        self.Bind(wx.EVT_SLIDER, self.shiftY, self.shiftYslider)
        self.Bind(wx.EVT_SLIDER, self.shiftZ, self.shiftZslider)

        self.Bind(wx.EVT_SLIDER, self.detail, self.detailslider)

    def set_ortho(self, event):
        self.canvas.ortho = True
        self.canvas.Refresh()

    def set_frust(self, event):
        self.canvas.ortho = False
        self.canvas.Refresh()

    def rotX(self, event):
        self.canvas.angX = self.rotXslider.GetValue()
        self.canvas.Refresh()

    def rotY(self, event):
        self.canvas.angY = self.rotYslider.GetValue()
        self.canvas.Refresh()

    def rotZ(self, event):
        self.canvas.angZ = self.rotZslider.GetValue()
        self.canvas.Refresh()

    def scaleX(self, event):
        self.canvas.scaleX = self.scaleXslider.GetValue() / 100
        self.canvas.Refresh()

    def scaleY(self, event):
        self.canvas.scaleY = self.scaleYslider.GetValue() / 100
        self.canvas.Refresh()

    def scaleZ(self, event):
        self.canvas.scaleZ = self.scaleZslider.GetValue() / 100
        self.canvas.Refresh()

    def shiftX(self, event):
        self.canvas.shiftX = self.shiftXslider.GetValue() / 100
        self.canvas.Refresh()

    def shiftY(self, event):
        self.canvas.shiftY = self.shiftYslider.GetValue() / 100
        self.canvas.Refresh()

    def shiftZ(self, event):
        self.canvas.shiftZ = self.shiftZslider.GetValue() / 100
        self.canvas.Refresh()

    def detail(self, event):
        self.canvas.figure.setDetail(self.detailslider.GetValue() * 2)
        self.canvas.Refresh()
