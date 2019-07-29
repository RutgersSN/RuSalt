## Activate rusalt environment.
## This is intended for extractions of four grating angles, run with python multiploy.py and 
## enter the desired directory path (/path/etc/x1d).
## This code is ugly and can probably be cleaned up.
## At lines 89,90, and 91 there are manual vertical lines.


import pyraf
from pyraf import iraf
from glob import glob
import os
import shutil

Path = raw_input('Destination to plots:')


if os.path.exists(Path+'/test/'):
	shutil.rmtree(Path+'/test/')
if os.path.exists(Path+'/test3/'):
	shutil.rmtree(Path+'/test3/')


def scopy():
    if not os.path.exists(Path+'/test/'):
        os.mkdir(Path+'/test/')
    fs= glob(Path+'/sci*c?.fits')
    print(fs)
    for i,f in enumerate(fs):
	iraf.scopy(f+'[*,1,1]',Path+'/test/'+'sci'+str(i)+'.fits')

def wspectext():
    if not os.path.exists(Path+'/test3/'):
        os.mkdir(Path+'/test3/')
    fs= glob(Path+'/test/'+'/sci*.fits')
    for i,f in enumerate(fs):
	iraf.cd(Path+'/test3/')
	iraf.wspectext(f,('sci'+str(i)+'.dat'))


import numpy as np
import matplotlib.pyplot as plot

scopy()
wspectext()

a= 'sci0.dat'
b= 'sci1.dat'
c= 'sci2.dat'
d= 'sci3.dat'
e= 'sci4.dat'
f= 'sci5.dat'
g= 'sci6.dat'
h= 'sci7.dat'
i= 'sci8.dat'
j= 'sci9.dat'
k= 'sci10.dat'
l= 'sci11.dat'





A= Path+'/test3/'+a
B= Path+'/test3/'+b
C= Path+'/test3/'+c
D= Path+'/test3/'+d
E= Path+'/test3/'+e
F= Path+'/test3/'+f
G= Path+'/test3/'+g
H= Path+'/test3/'+h
I= Path+'/test3/'+i
J= Path+'/test3/'+j
K= Path+'/test3/'+k
L= Path+'/test3/'+l


plot.plot(*np.loadtxt(A,unpack=True), linewidth=2.0, label=a)
plot.plot(*np.loadtxt(B,unpack=True), linewidth=2.0, label=b)
plot.plot(*np.loadtxt(C,unpack=True), linewidth=2.0, label=c)
plot.plot(*np.loadtxt(D,unpack=True), linewidth=2.0, label=d)
plot.plot(*np.loadtxt(E,unpack=True), linewidth=2.0, label=e)
plot.plot(*np.loadtxt(F,unpack=True), linewidth=2.0, label=f)
plot.plot(*np.loadtxt(G,unpack=True), linewidth=2.0, label=g)
plot.plot(*np.loadtxt(H,unpack=True), linewidth=2.0, label=h)
plot.plot(*np.loadtxt(I,unpack=True), linewidth=2.0, label=i)
plot.plot(*np.loadtxt(J,unpack=True), linewidth=2.0, label=j)
plot.plot(*np.loadtxt(K,unpack=True), linewidth=2.0, label=k)
plot.plot(*np.loadtxt(L,unpack=True), linewidth=2.0, label=l)

plot.axvline(x=4410)
plot.axvline(x=4256)
plot.axvline(x=4886)
plot.legend()

plot.show()
