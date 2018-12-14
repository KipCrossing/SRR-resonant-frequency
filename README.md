# SSR  Resonant Frequency

Functions to help calculate the resonant frequencies of split ring resonators (SSR).
## Getting Started

```
git clone https://github.com/KipCrossing/SRR-resonant-frequency
```

### Usage

See [example.py](https://github.com/KipCrossing/SRR-resonant-frequency/blob/master/example.py) to get started or copy srr.py into your working directory.

Import SplitRing

```python
from srr import SplitRing
```

SplitRing takes 4 arguments
* 1 the ring gap
* 2 the ring height
* 3 the ring width
* 4 the ring radius

for example:

```python
SR = SplitRing(0.003,0.0008,0.0008,0.001)   # SplitRing(gap,height,width,radius)
```

To get the resonant frequency:

```python
RF = SR.ResonantFrequency()
```

Other useful properties include:

```python
SR.permittivity     # permittivity of free space
SR.permeability     # permeability of free space  
SR.Inductance()     # inductance of the SRR
SR.C_gap()          # gap capacitance of the SRR
SR.C_surf()         # surface capacitance of the SRR
SR.Capacitance()    # total capacitance of the SRR
```

## Acknowledgements
Written By Kipling Crossing

Inspired by the paper "Analytical formulation for the resonant frequency of split rings" (Sydoruk et al.)
