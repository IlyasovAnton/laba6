import wx
from wx import glcanvas
from OpenGL.GLU import *

from Figures import *


class OpenGlCanvas(glcanvas.GLCanvas):
    def __init__(self, parent):
        self.size = (800, 800)
        glcanvas.GLCanvas.__init__(self, parent, -1, size=self.size)
        self.context = glcanvas.GLContext(self)
        self.SetCurrent(self.context)

        self.axis = True
        self.ortho = False

        self.distanse = 2

        self.angX = 0
        self.angY = 0
        self.angZ = 0

        self.scaleX = 1
        self.scaleY = 1
        self.scaleZ = 1

        self.shiftX = 0
        self.shiftY = 0
        self.shiftZ = 0

        self.angE1 = 0
        self.angE2 = 0
        self.eye_start = np.array([-1.0, 0.5, 1.0])

        self.figure = Figure(0.2, 0.25, 0.3, 0.05, 0.1, 0.04, 20)

        self.Bind(wx.EVT_PAINT, self.OnDraw)
        self.Bind(wx.EVT_MOTION, self.move_camera)
        self.Bind(wx.EVT_MOUSEWHEEL, self.set_distanse)

    def OnDraw(self, event):
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_FLAT)
        glEnable(GL_CULL_FACE)

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        self.draw()
        self.SwapBuffers()

    def draw(self):
        if not self.ortho:
            gluPerspective(45.0, 1, 0.5, 10.0)
        else:
            glOrtho(-1, 1, -1, 1, 0.5, 10.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.eye = rotate(self.eye_start, self.angE1, self.angE2)

        gluLookAt(self.eye[0] * self.distanse, self.eye[1] * self.distanse, self.eye[2] * self.distanse,
                  0.0, 0.0, 0.0,
                  0.0, 1.0, 0.0)

        if self.axis:
            draw_axis()

        glScale(self.scaleX, self.scaleY, self.scaleZ)
        glTranslate(self.shiftX, self.shiftY, self.shiftZ)

        glRotatef(self.angX, 1, 0, 0)
        glRotatef(self.angY, 0, 1, 0)
        glRotatef(self.angZ, 0, 0, 1)

        self.figure.draw()

    def move_camera(self, event):
        if event.LeftIsDown():
            pos = event.GetPosition()
            self.angE1 = (pos[0] - 400) * 0.45
            self.angE2 = (400 - pos[1]) * 0.225
        self.Refresh()

    def set_distanse(self, event):
        self.distanse -= 0.1 * np.sign(event.GetWheelRotation())
        self.Refresh()
