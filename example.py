from srr import SplitRing

SR = SplitRing(200,50,50,800)

RF = SR.ResonantFrequency()
print(RF)

# Other useful properties include:
SR.permittivity     # permittivity of free space
SR.permeability     # permeability of free space
SR.Inductance()     # indictance of the SRR
SR.C_gap()          # gap capacitance of the SRR
SR.C_surf()         # surface capacitance of the SRR
SR.Capacitance()    # total capacitance of the SRR