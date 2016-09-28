import mahotas as mh
import numpy as np
from pylab import imshow, show
import scipy as sp
import scipy.ndimage

def grayscaleLabel():
    f = scipy.ndimage.imread
    ('/Users/ChinasaOkolo/Google Drive/REU Project/
    Grayscale Segmented Z-Stack WT6 hrs infected 40x/WT6 hrs infectedZ41C1.tif')

    f = f[:,:,0]
    imshow(f)
    show()

    f = mh.gaussian_filter(f, 4)
    f = (f> f.mean())
    imshow(f)
    show()

    labeled, n_nucleus  = mh.label(f)
    print('Found {} nuclei.'.format(n_nucleus))
    imshow(labeled)
    show()

    sizes = mh.labeled.labeled_size(labeled)
    too_big = np.where(sizes > 10000)
    labeled = mh.labeled.remove_regions(labeled, too_big)
    imshow(labeled)
    show()

    labeled = mh.labeled.remove_bordering(labeled)
    imshow(labeled)
    show()

    relabeled, n_left = mh.labeled.relabel(labeled)
    print('After filtering and relabeling, there are {} nuclei left.'.format(n_left))
    imshow(relabeled)
    show()

    import pylab
    print f.shape

    print f.dtype
    print f.max()
    print f.min()

    pylab.imshow(f // 2)
    pylab.show()

    f = (f*255).astype('uint8')
    T = mh.thresholding.otsu(f)
    pylab.imshow(f > T)
    imshow(f)
    show()

    pylab.gray()
    show()
    
    print f.shape
    print f.dtype
    print f.max()
    print f.min()

    pylab.imshow(f // 2)
    pylab.show()
    T = mh.thresholding.otsu(f)
    pylab.imshow(f > T)
    pylab.show()
    
    ff = (ff*255).astype('uint8')
    T = mh.thresholding.otsu(ff)
    pylab.imshow(ff > T)
    pylab.show()

    pylab.imshow(ff > T)
    pylab.show()
    labeled,nr_objects = mh.label(ff > T)
    print nr_objects

    pylab.imshow(labeled)
    pylab.jet()
    pylab.show()
    
    ff = mh.gaussian_filter(f, 8)
    rmax = mh.regmax(ff)
    pylab.imshow(mh.overlay(f, rmax))
    pylab.show()

    ff = mh.gaussian_filter(f, 16)
    rmax = mh.regmax(ff)
    pylab.imshow(mh.overlay(f, rmax))
    pylab.show()

    seeds,nr_nuclei = mh.label(rmax)
    print nr_nuclei
    ff = (ff*255).astype('uint8')
    T = mh.thresholding.otsu(ff)

    dist = mh.distance(ff > T)
    dist = dist.max() - dist
    dist -= dist.min()
    dist = dist/float(dist.ptp()) * 255
    dist = dist.astype(np.uint8)
    pylab.imshow(dist)
    pylab.show()

    nuclei = mh.cwatershed(dist, seeds)
    pylab.imshow(nuclei)
    pylab.show()
    whole = mh.segmentation.gvoronoi(nuclei)
    pylab.imshow(whole)
    pylab.show()

    


    


    
