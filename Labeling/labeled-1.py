import mahotas as mh
import numpy as np
from pylab import imshow, show

regions = np.zeros((8,8), bool)

regions[:3,:3] = 1
regions[6:,6:] = 1
labeled, nr_objects = mh.label(regions)

imshow(labeled, interpolation='nearest')
show()
