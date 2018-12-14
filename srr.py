# By Kipling Crossing
# github.com/KipCrossing
import math

class SplitRing(object):
    """Described a split ring and its assosiated properties for split ring resinator (SRR) applications. inspired by the paper 'Analytical formulation for the resonant frequency of split rings' """

    def __init__(self,gap,height,width,radius):
        """Short summary.

        Parameters
        ----------
        gap : float
            The size of the gap in the ring.
        height : float
            The height if the ring.
        width : float
            The width of the ring.
        radius : float
            the radius of the ring. From center to inner side of the ring.
        """
        self.gap = gap
        self.height = height
        self.width = width
        self.radius = radius

    @property
    def permittivity(self):
        """str: permittivity of free space"""
        return 8.854187817*(10**-12)   #E0

    @property
    def permeability(self):
        """str: permeability of free space"""
        return math.pi*4*(10**-7)      #u0

    def Inductance(self):
        """Returns:
            float: the indictance of the SRR"""
        Rm = self.radius + (self.width/2)
        L = Rm*self.permeability*(math.log(8*Rm/(self.height+self.width))-0.5)
        return L

    def C_gap(self):
        """Returns:
            float: the gap capacitance of the SRR"""
        Co = self.permittivity*(self.height+self.width+self.gap)
        C = self.permittivity*(self.height*self.width/self.gap)+ Co
        return C

    def C_surf(self):
        """Returns:
            float: the surface capacitance of the SRR"""
        C = (2*self.permittivity*(self.height + self.width)/math.pi)*math.log(4*self.radius/self.gap)
        return C

    def Capacitance(self):
        """Returns:
            float: the total capacitance of the SRR"""
        return self.C_gap() + self.C_surf()

    def ResonantFrequency(self):
        """Returns:
            float: the resonant frequency of the SRR"""
        f = 1/(2*math.pi*math.sqrt(self.Inductance()*self.Capacitance()))
        return f
