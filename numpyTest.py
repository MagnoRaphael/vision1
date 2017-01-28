import numpy as np
from numpy import pi

a = np.array( [[20,30,40,50],[20,30,40,50]] )

a[0,0] = 55

a = a.flatten()

print(a)