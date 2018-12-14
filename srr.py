# By Kipling Crossing
# github.com/KipCrossing
import math

class SplitRing(object):
    _permittivity = 8.854187817*(10**-12)   #E0
    _permeability = math.pi*4*(10**-6)      #u0

    def __init__(self,gap,height,width,radius):
        self.gap = gap
        self.height = height
        self.width = width
        self.radius = radius

    def Inductance(self):
        Rm = self.radius + (self.width/2)
        L = Rm*self._permeability*(math.log(8*Rm/(self.height+self.width))-0.5)
        return L

    def C_gap(self):
        Co = self._permittivity*(self.height+self.width+self.gap)
        C = self._permittivity*(self.height*self.width/self.gap)+ Co
        return C

    def C_surf(self):
        C = (2*self._permittivity*(self.height + self.width)/math.pi)*math.log(4*self.radius/self.gap)
        return C

    def Capacitance(self):
        return self.C_gap() + self.C_surf()

    def ResonantFrequency(self):
        f = 1/(2*math.pi*math.sqrt(self.Inductance()*self.Capacitance()))
        return f

SR = SplitRing(5,1,1,20)

print(SR.ResonantFrequency())
