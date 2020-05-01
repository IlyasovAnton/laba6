import numpy as np
from OpenGL.GL import *


class Cylinder:
    def __init__(self, center1, center2, radius, detail):
        """
        :param center1: coordinate of the first base of the cylinder
        :param center2: coordinate of the second base of the cylinder
        :param radius: cylinder radius
        :param detail: number of dots per circle
        """
        self.x1 = center1[0]
        self.y1 = center1[1]
        self.z1 = center1[2]

        self.x2 = center2[0]
        self.y2 = center2[1]
        self.z2 = center2[2]

        self.r = radius
        self.d = detail

        self.verticesArray = []
        self.init_vertex_array()

        self.indicesArray = []
        self.init_indices_array()

    def init_vertex_array(self):
        if self.z1 != self.z2:
            for i in range(self.d):
                ang1 = 2 * np.pi * i / self.d
                self.verticesArray.append(self.r * np.cos(ang1) + self.x1)
                self.verticesArray.append(self.r * np.sin(ang1) + self.y1)
                self.verticesArray.append(self.z1)
            for i in range(self.d):
                ang1 = 2 * np.pi * i / self.d
                self.verticesArray.append(self.r * np.cos(ang1) + self.x2)
                self.verticesArray.append(self.r * np.sin(ang1) + self.y2)
                self.verticesArray.append(self.z2)
        elif self.x1 != self.x2:
            for i in range(self.d):
                ang1 = 2 * np.pi * i / self.d
                self.verticesArray.append(self.x1)
                self.verticesArray.append(self.r * np.cos(ang1) + self.y1)
                self.verticesArray.append(self.r * np.sin(ang1) + self.z1)
            for i in range(self.d):
                ang1 = 2 * np.pi * i / self.d
                self.verticesArray.append(self.x2)
                self.verticesArray.append(self.r * np.cos(ang1) + self.y2)
                self.verticesArray.append(self.r * np.sin(ang1) + self.z2)
        elif self.y1 != self.y2:
            for i in range(self.d):
                ang1 = 2 * np.pi * i / self.d
                self.verticesArray.append(self.r * np.cos(ang1) + self.x1)
                self.verticesArray.append(self.y1)
                self.verticesArray.append(self.r * np.sin(ang1) + self.z1)
            for i in range(self.d):
                ang1 = 2 * np.pi * i / self.d
                self.verticesArray.append(self.r * np.cos(ang1) + self.x2)
                self.verticesArray.append(self.y2)
                self.verticesArray.append(self.r * np.sin(ang1) + self.z2)

    def init_indices_array(self):
        for i in range(self.d):
            self.indicesArray.append(np.mod(i, self.d))
            self.indicesArray.append(np.mod(np.mod(i, self.d) + 1, self.d))

            self.indicesArray.append(np.mod(i, self.d) + self.d)
            self.indicesArray.append(np.mod(np.mod(i, self.d) + 1, self.d) + self.d)

            self.indicesArray.append(np.mod(i, self.d))
            self.indicesArray.append(np.mod(i, self.d) + self.d)

            self.indicesArray.append(np.mod(np.mod(i, self.d) + 1, self.d))
            self.indicesArray.append(np.mod(np.mod(i, self.d) + 1, self.d) + self.d)

    def crop(self, cropping_radius, axis1, axis2):
        for i in range(0, len(self.verticesArray) // 2, 3):
            self.verticesArray[i + axis1] = np.sqrt(np.square(cropping_radius) -
                                                    np.square(self.verticesArray[i + axis2]))
        for i in range(len(self.verticesArray) // 2, len(self.verticesArray), 3):
            self.verticesArray[i + axis1] = -np.sqrt(np.square(cropping_radius) -
                                                     np.square(self.verticesArray[i + axis2]))

    def draw(self):
        glEnableClientState(GL_VERTEX_ARRAY)

        glVertexPointer(3, GL_FLOAT, 0, self.verticesArray)
        glDrawElements(GL_LINES, len(self.indicesArray), GL_UNSIGNED_BYTE, self.indicesArray)

        glDisableClientState(GL_VERTEX_ARRAY)


class ArbitraryCylinder:
    def __init__(self, center1, center2, radius, detail):
        self.x1 = center1[0]
        self.y1 = center1[1]
        self.z1 = center1[2]

        self.x2 = center2[0]
        self.y2 = center2[1]
        self.z2 = center2[2]

        self.r = radius
        self.d = detail

        self.verticesArray = []
        self.init_vertex_array()

        self.indicesArray = []
        self.init_indices_array()

    def init_vertex_array(self):
        for i in range(self.d // 2 + 1):
            ang1 = 2 * np.pi * i / self.d
            self.verticesArray.append(self.r * np.sin(ang1) + self.x1)
            self.verticesArray.append(self.y1)
            self.verticesArray.append(self.r * np.cos(ang1) + self.z2)
        for i in range(self.d // 2 + 1):
            ang1 = 2 * np.pi - 2 * np.pi * i / self.d
            self.verticesArray.append(self.r * np.sin(ang1) + self.x2)
            self.verticesArray.append(self.y1)
            self.verticesArray.append(self.z2 - self.r * np.cos(ang1))
        for i in range(self.d // 2 + 1):
            ang1 = 2 * np.pi * i / self.d
            self.verticesArray.append(self.r * np.sin(ang1) + self.x1)
            self.verticesArray.append(self.y2)
            self.verticesArray.append(self.r * np.cos(ang1) + self.z2)
        for i in range(self.d // 2 + 1):
            ang1 = 2 * np.pi - 2 * np.pi * i / self.d
            self.verticesArray.append(self.r * np.sin(ang1) + self.x2)
            self.verticesArray.append(self.y2)
            self.verticesArray.append(self.z2 - self.r * np.cos(ang1))

    def init_indices_array(self):
        for i in range(self.d + 2):
            self.indicesArray.append(np.mod(i, 2 + self.d))
            self.indicesArray.append(np.mod(np.mod(i, 2 + self.d) + 1, 2 + self.d))

            self.indicesArray.append(np.mod(i, 2 + self.d) + 2 + self.d)
            self.indicesArray.append(np.mod(np.mod(i, 2 + self.d) + 1, 2 + self.d) + 2 + self.d)

            self.indicesArray.append(np.mod(i, 2 + self.d))
            self.indicesArray.append(np.mod(i, 2 + self.d) + 2 + self.d)

            self.indicesArray.append(np.mod(np.mod(i, 2 + self.d) + 1, 2 + self.d))
            self.indicesArray.append(np.mod(np.mod(i, 2 + self.d) + 1, 2 + self.d) + 2 + self.d)

    def crop(self, cropping_radius, axis1, axis2):
        for i in range(0, len(self.verticesArray) // 2, 3):
            self.verticesArray[i + axis1] = np.sqrt(np.square(cropping_radius) -
                                                    np.square(self.verticesArray[i + axis2]))

    def draw(self):
        glEnableClientState(GL_VERTEX_ARRAY)

        glVertexPointer(3, GL_FLOAT, 0, self.verticesArray)
        glDrawElements(GL_LINES, len(self.indicesArray), GL_UNSIGNED_BYTE, self.indicesArray)

        glDisableClientState(GL_VERTEX_ARRAY)


class Figure:
    def __init__(self, r1, r2, r3, r4, r5, r6, detail):
        """
        :param r1: radius of the first cylinder
        :param r2: radius of the second cylinder
        :param r3: radius of the third cylinder
        :param r4: radius of the fourth cylinder
        :param r5: radius of the fifth cylinder
        :param r6: radius of the sixth cylinder
        :param detail: number of dots per circle
        """
        self.params = [r1, r2, r3, r4, r5, r6]

        self.cylinder1 = None
        self.cylinder2 = None
        self.cylinder3 = None
        self.cylinder4 = None
        self.cylinder5 = None
        self.cylinder6 = None
        self.arbitrary_cylinder = None

        self.init(r1, r2, r3, r4, r5, r6, detail)

    def init(self, r1, r2, r3, r4, r5, r6, detail):
        self.cylinder1 = Cylinder((-0.9, 0, 0), (-0.4, 0, 0), r1, detail)
        self.cylinder2 = Cylinder((-0.4, 0, 0), (0.4, 0, 0), r2, detail)
        self.cylinder3 = Cylinder((0.4, 0, 0), (0.9, 0, 0), r3, detail)

        self.cylinder4 = Cylinder((-0.65, r1, 0), (-0.65, -r1, 0), r4, detail // 2)
        self.cylinder4.crop(r1, 1, 2)
        self.cylinder5 = Cylinder((0.65, r3, 0), (0.65, -r3, 0), r5, detail // 2)
        self.cylinder5.crop(r3, 1, 2)
        self.cylinder6 = Cylinder((0.65, 0, r3), (0.65, 0, -r3), r5, detail // 2)
        self.cylinder6.crop(r3, 2, 1)
        self.arbitrary_cylinder = ArbitraryCylinder((0, r2, 0), (-0.3, r2 - 0.05, 0), r6, detail)
        self.arbitrary_cylinder.crop(r2, 1, 2)

    def setDetail(self, detail):
        self.init(*self.params, detail)

    def draw(self):
        self.cylinder1.draw()
        self.cylinder2.draw()
        self.cylinder3.draw()
        self.cylinder4.draw()
        self.cylinder5.draw()
        self.cylinder6.draw()
        self.arbitrary_cylinder.draw()


def draw_axis():
    colorArray = [0., 0., 0.,
                  1., 0., 0.,
                  0., 1., 0.,
                  0., 0., 1.]
    vertexArray = [0., 0., 0.,
                   0.4, 0., 0.,
                   0., 0.4, 0.,
                   0., 0., 0.4]
    indicesArray = [0, 1,
                    0, 2,
                    0, 3]

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)

    glVertexPointer(3, GL_FLOAT, 0, vertexArray)
    glColorPointer(3, GL_FLOAT, 0, colorArray)
    glDrawElements(GL_LINES, len(indicesArray), GL_UNSIGNED_BYTE, indicesArray)

    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)


def rotate(vec, alpha, beta):
    M11 = np.cos(np.pi * alpha / 180)
    M12 = np.sin(np.pi * alpha / 180) * np.cos(np.pi * beta / 180)
    M13 = np.sin(np.pi * alpha / 180) * np.sin(np.pi * beta / 180)
    M21 = -np.sin(np.pi * alpha / 180)
    M22 = np.cos(np.pi * alpha / 180) * np.cos(np.pi * beta / 180)
    M23 = np.cos(np.pi * alpha / 180) * np.sin(np.pi * beta / 180)
    M31 = 0
    M32 = -np.sin(np.pi * beta / 180)
    M33 = np.cos(np.pi * beta / 180)

    rotated = np.dot(vec, np.array([[M11, M12, M13],
                                    [M21, M22, M23],
                                    [M31, M32, M33]]))
    return rotated


def rotate1(vec, alpha, axis):
    x = axis[0]
    y = axis[2]
    z = axis[1]

    M11 = np.cos(np.pi * alpha / 180) * (1 - np.square(x)) + np.square(x)
    M12 = x * (1 - np.cos(np.pi * alpha / 180)) * y + z * np.sin(np.pi * alpha / 180)
    M13 = x * (1 - np.cos(np.pi * alpha / 180)) * z - y * np.sin(np.pi * alpha / 180)
    M21 = x * (1 - np.cos(np.pi * alpha / 180)) * y
    M22 = np.cos(np.pi * alpha / 180) * (1 - np.square(y)) + np.square(y)
    M23 = y * (1 - np.cos(np.pi * alpha / 180)) * z + x * np.sin(np.pi * alpha / 180)
    M31 = x * (1 - np.cos(np.pi * alpha / 180)) * z + y * np.sin(np.pi * alpha / 180)
    M32 = y * (1 - np.cos(np.pi * alpha / 180)) * z - x * np.sin(np.pi * alpha / 180)
    M33 = np.cos(np.pi * alpha / 180) * (1 - np.square(z)) + np.square(z)

    rotated = np.dot(vec, np.array([[M11, M12, M13],
                                    [M21, M22, M23],
                                    [M31, M32, M33]]))
    return rotated


def rotate2(vec, alpha, beta):
    vec = rotX(vec, beta)
    vec = rotY(vec, alpha)

    return vec


def rotX(vec, alpha):
    return np.dot(vec,
                  np.array([[1., 0., 0.],
                            [0., np.cos(np.pi * alpha / 180), -np.sin(np.pi * alpha / 180)],
                            [0., np.sin(np.pi * alpha / 180), np.cos(np.pi * alpha / 180)]]))


def rotY(vec, alpha):
    return np.dot(vec,
                  np.array([[np.cos(np.pi * alpha / 180), 0., np.sin(np.pi * alpha / 180)],
                            [0., 1., 0.],
                            [-np.sin(np.pi * alpha / 180), 0, np.cos(np.pi * alpha / 180)]]))


def rotZ(vec, alpha):
    return np.dot(vec,
                  np.array([[np.cos(np.pi * alpha / 180), -np.sin(np.pi * alpha / 180), 0.],
                            [np.sin(np.pi * alpha / 180), np.cos(np.pi * alpha / 180), 0.],
                            [0., 0., 1.]]))
