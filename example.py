from srr import SplitRing

gap    = 0.0015
height = 0.0005
width  = 0.0005
radius = 0.01


SR = SplitRing(gap,height,width,radius) # Units in m

RF = SR.ResonantFrequency()

print('Resonant Frequency: %f GHz' % (RF/10**9))
# Resonant Frequency: 3.457072 GHz

# Other useful properties include:
SR.permittivity     # permittivity of free space
SR.permeability     # permeability of free space
SR.Inductance()     # indictance of the SRR
SR.C_gap()          # gap capacitance of the SRR
SR.C_surf()         # surface capacitance of the SRR
SR.Capacitance()    # total capacitance of the SRR
