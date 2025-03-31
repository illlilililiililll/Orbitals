import numpy as np

# Constants
a0 = 1.0
Z = 1.0

def sigma(r):
    return 2*Z*r/a0

# R
class R:
    @staticmethod
    def _1s(r, a0=a0, Z=Z):
        return 2 * Z**(3/2) * np.exp(-sigma(r)/2)

    @staticmethod
    def _2s(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1 / (2 * np.sqrt(2))) * Z**(3/2) * (2 - s) * np.exp(-s/2)
    
    @staticmethod
    def _2p(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1 / (2 * np.sqrt(6))) * Z**(3/2) * s * np.exp(-s/2)

    @staticmethod
    def _3s(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1 / (9 * np.sqrt(3))) * Z**(3/2) * (6 - 6*s + s**2) * np.exp(-s/2)

    @staticmethod
    def _3p(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1 / (9 * np.sqrt(6))) * Z**(3/2) * (4 - s) * s * np.exp(-s/2)

    @staticmethod
    def _3d(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1 / (9 * np.sqrt(30))) * Z**(3/2) * s**2 * np.exp(-s/2)
    
    @staticmethod
    def _4s(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1/96) * Z**(3/2) * (24 - 36*s + 12*s**2 - s**3) * np.exp(-s/2)
    
    @staticmethod
    def _4p(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1/(32 * np.sqrt(15))) * Z**(3/2) * (20 - 10*s + s**2) * s * np.exp(-s/2)

    @staticmethod
    def _4d(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1/(96 * np.sqrt(5))) * Z**(3/2) * (6 - s) * s**2 * np.exp(-s/2)

    @staticmethod
    def _4f(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1/(96 * np.sqrt(35))) * Z**(3/2) * s**3 * np.exp(-s/2)
    
    @staticmethod
    def _5s(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1/(300 * np.sqrt(5))) * Z**(3/2) * (120 - 240*s + 120*s**2 - 20*s**3 + s**4) * np.exp(-s/2)
    
    @staticmethod
    def _5p(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1/(150 * np.sqrt(30))) * Z**(3/2) * (120 - 90*s + 18*s**2 - s**3) * s * np.exp(-s/2)

    @staticmethod
    def _5d(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1/(150 * np.sqrt(70))) * Z**(3/2) * (42 - 14*s + s**2) * s**2 * np.exp(-s/2)

    @staticmethod
    def _5f(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1/(300 * np.sqrt(70))) * Z**(3/2) * (8 - s) * s**3 * np.exp(-s/2)

    @staticmethod
    def _5g(r, a0=a0, Z=Z):
        s = sigma(r)
        return (1/(900 * np.sqrt(70))) * Z**(3/2) * s**4 * np.exp(-s/2)
        
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
        return np.sqrt(15 / (16 * np.pi)) * np.sin(theta)**2 * np.sin(2*phi)

    @staticmethod
    def dxz(theta, phi):
        return np.sqrt(15 / (4 * np.pi)) * np.sin(theta) * np.cos(theta) * np.cos(phi)

    @staticmethod
    def dyz(theta, phi):
        return np.sqrt(15 / (4 * np.pi)) * np.sin(theta) * np.cos(theta) * np.sin(phi)

    @staticmethod
    def dx2y2(theta, phi):
        return np.sqrt(15 / (16 * np.pi)) * np.sin(theta)**2 * np.cos(2*phi)
    
    @staticmethod
    def fz3(theta, phi):
        return np.sqrt(7 / (16 * np.pi)) * np.cos(theta) * (5 * np.cos(theta)**2 - 3)
    
    @staticmethod
    def fyz2(theta, phi):
        return np.sqrt(21 / (8 * np.pi)) * np.sin(theta) * np.sin(phi) * (5*np.cos(theta)**2 - 1)
    
    @staticmethod
    def fxz2(theta, phi):
        return np.sqrt(21 / (8 * np.pi)) * np.sin(theta) * np.cos(phi) * (5*np.cos(theta)**2 - 1)
    
    @staticmethod
    def fxyz(theta, phi):
        return np.sqrt(105 / (4 * np.pi)) * np.sin(theta)**2 * np.cos(theta) * np.sin(phi) * np.cos(phi)
    
    @staticmethod
    def fzx2y2(theta, phi):
        return np.sqrt(105 / (16 * np.pi)) * np.cos(theta) * np.sin(theta)**2 * np.cos(2*phi)
    
    @staticmethod
    def fy3x2y2(theta, phi):
        return np.sqrt(35 / (4 * np.pi)) * np.sin(theta)**3 * np.sin(phi) * (3 * np.cos(phi)**2 - 1)
    
    @staticmethod
    def fxx23y2(theta, phi):
        return np.sqrt(35 / (4 * np.pi)) * np.sin(theta)**3 * np.cos(phi) * (np.cos(phi)**2 - 3 * np.sin(phi)**2)
    
    @staticmethod
    def gz4(theta, phi):
        return np.sqrt(9 / (64 * np.pi)) * (35 * np.cos(theta)**4 - 30 * np.cos(theta)**2 + 3)

    @staticmethod
    def gz3y(theta, phi):
        return np.sqrt(45 / (8 * np.pi)) * np.sin(theta) * np.cos(theta) * (7 * np.cos(theta)**2 - 3) * np.sin(phi)

    @staticmethod
    def gz3x(theta, phi):
        return np.sqrt(45 / (8 * np.pi)) * np.sin(theta) * np.cos(theta) * (7 * np.cos(theta)**2 - 3) * np.cos(phi)

    @staticmethod
    def gz2xy(theta, phi):
        return np.sqrt(45 / (16 * np.pi)) * np.sin(theta)**2 * (7 * np.cos(theta)**2 - 1) * np.sin(2 * phi)

    @staticmethod
    def gz2x2y2(theta, phi):
        return np.sqrt(45 / (16 * np.pi)) * np.sin(theta)**2 * (7 * np.cos(theta)**2 - 1) * np.cos(2 * phi)

    @staticmethod
    def gzy3(theta, phi):
        return np.sqrt(315 / (8 * np.pi)) * np.sin(theta)**3 * np.cos(theta) * (3 * np.cos(phi)**2 - 1) * np.sin(phi)

    @staticmethod
    def gzx3(theta, phi):
        return np.sqrt(315 / (8 * np.pi)) * np.sin(theta)**3 * np.cos(theta) * (np.cos(phi)**2 - 3 * np.sin(phi)**2) * np.cos(phi)

    @staticmethod
    def gxyx2y2(theta, phi):
        return np.sqrt(315 / (64 * np.pi)) * np.sin(theta)**4 * np.sin(2 * phi) * (np.cos(phi)**2 - np.sin(phi)**2)

    @staticmethod
    def gx4y4(theta, phi):
        return np.sqrt(315 / (64 * np.pi)) * np.sin(theta)**4 * (np.cos(phi)**4 + np.sin(phi)**4 - 6 * np.cos(phi)**2 * np.sin(phi)**2)
        
class Orbital:
    combinations = {
        R._1s: [Y.s],
        R._2s: [Y.s],
        R._3s: [Y.s],
        R._2p: [Y.px, Y.py, Y.pz],
        R._3p: [Y.px, Y.py, Y.pz],
        R._3d: [Y.dz2, Y.dxy, Y.dxz, Y.dyz, Y.dx2y2],
        R._4s: [Y.s],
        R._4p: [Y.px, Y.py, Y.pz],
        R._4d: [Y.dz2, Y.dxy, Y.dxz, Y.dyz, Y.dx2y2],
        R._4f: [Y.fz3, Y.fyz2, Y.fxz2, Y.fxyz, Y.fzx2y2, Y.fy3x2y2, Y.fxx23y2],  # 확장 가능
        R._5s: [Y.s],
        R._5p: [Y.px, Y.py, Y.pz], 
        R._5d: [Y.dz2, Y.dxy, Y.dxz, Y.dyz, Y.dx2y2],
        R._5f: [Y.fz3, Y.fyz2, Y.fxz2, Y.fxyz, Y.fzx2y2, Y.fy3x2y2, Y.fxx23y2],  # 확장 가능
        R._5g: [Y.gz4, Y.gz3y, Y.gz3x, Y.gz2xy, Y.gz2x2y2, Y.gzy3, Y.gzx3, Y.gxyx2y2, Y.gx4y4],  # 확장 가능
    }

    def __init__(self, r, y):
        self.r = r
        self.y = y

        if y not in self.combinations.get(r, []):
            raise ValueError("Invalid R and Y function combination")