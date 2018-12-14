from srr import SplitRing

SR = SplitRing(0.004,0.001,0.001,0.015) # Units in m

RF = SR.ResonantFrequency()

print('Resonant Frequency: %f GHz' % (RF/10**9))
# Resonant Frequency: 2.043394 GHz

# Other useful properties include:
SR.permittivity     # permittivity of free space
SR.permeability     # permeability of free space
SR.Inductance()     # indictance of the SRR
SR.C_gap()          # gap capacitance of the SRR
SR.C_surf()         # surface capacitance of the SRR
SR.Capacitance()    # total capacitance of the SRR
