import numpy as np

# Constants
a0 = 1.0
Z = 1.0

def sigma(r):
    return Z*r/a0

class Orbital:
    def __init__(self, r, y):
        self.r = r
        self.y = y

        if ((y==Y.s) and (r not in [R._1s, R._2s, R._3s])) or ((r==R._2p or r==R._3p) and (y not in [Y.px, Y.py, Y.pz])) or ((r==R._3d) and (y not in [Y.dz2, Y.dxy, Y.dxz, Y.dyz, Y.dx2y2])):
            raise ValueError("Invalid R and Y function combination")

# R
class R:
    @staticmethod
    def _1s(r, a0=a0, Z=Z):
        return 2 * (Z / a0)**(3/2) * np.exp(-sigma(r))

    @staticmethod
    def _2s(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1 / (2 * np.sqrt(2))) * (Z / a0)**(3/2) * (2 - s) * np.exp(-s/2)

    @staticmethod
    def _3s(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1 / (81 * np.sqrt(3))) * (Z / a0)**(3/2) * (27 - 18*s + 2*s**2) * np.exp(-s/3)

    @staticmethod
    def _2p(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1 / (2 * np.sqrt(6))) * (Z / a0)**(3/2) * s * np.exp(-s/2)

    @staticmethod
    def _3p(r, a0=a0, Z=Z):
        s = sigma(r)
        return (4 / (81 * np.sqrt(6))) * (Z / a0)**(3/2) * (6 - s) * s * np.exp(-s/3)

    @staticmethod
    def _3d(r, a0=a0, Z=Z):
        s = sigma(r)
        return (4 / (81 * np.sqrt(30))) * (Z / a0)**(3/2) * s**2 * np.exp(-s/3)

# Y
class Y:
    @staticmethod
    def s(theta, phi):
        return 1 / np.sqrt(4 * np.pi)

    @staticmethod
    def px(theta, phi):
        return np.sqrt(3 / (4 * np.pi)) * np.sin(theta) * np.cos(phi)

    @staticmethod
    def py(theta, phi):
        return np.sqrt(3 / (4 * np.pi)) * np.sin(theta) * np.sin(phi)

    @staticmethod
    def pz(theta, phi):
        return np.sqrt(3 / (4 * np.pi)) * np.cos(theta)

    @staticmethod
    def dz2(theta, phi):
        return np.sqrt(5 / (16 * np.pi)) * (3 * np.cos(theta)**2 - 1)

    @staticmethod
    def dxy(theta, phi):
        return np.sqrt(15 / (16 * np.pi)) * np.sin(theta)**2 * np.cos(2*phi)

    @staticmethod
    def dxz(theta, phi):
        return np.sqrt(15 / (4 * np.pi)) * np.sin(theta) * np.cos(theta) * np.cos(phi)

    @staticmethod
    def dyz(theta, phi):
        return np.sqrt(15 / (4 * np.pi)) * np.sin(theta) * np.cos(theta) * np.sin(phi)

    @staticmethod
    def dx2y2(theta, phi):
        return np.sqrt(15 / (16 * np.pi)) * np.sin(theta)**2 * np.cos(2*phi)