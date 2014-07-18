import numpy as np
import erfa.cython_numpy as erfa

jd = np.linspace(2456855.5, 2456855.5+1.0/24.0/60.0, 60*2+1)
ra  = np.linspace(0.0,np.pi*2.0,5)
dec = np.linspace(-np.pi/2.0,+np.pi/2.0,4) 

aob, zob, hob, dob, rob, eo = erfa.atco13(0.0,0.0,0.0,0.0,0.0,0.0,jd,0.0,0.0,0.0,np.pi/4.0,0.0,0.0,0.0,1014.0,0.0,0.0,0.5)
print(aob.shape)

aob, zob, hob, dob, rob, eo = erfa.atco13(0.0,0.0,0.0,0.0,0.0,0.0,jd[0],0.0,0.0,0.0,np.pi/4.0,0.0,0.0,0.0,1014.0,0.0,0.0,0.5)
print(aob.shape)

aob, zob, hob, dob, rob, eo = erfa.atco13(ra[:,None,None],dec[None,:,None],0.0,0.0,0.0,0.0,jd[None,None,:],0.0,0.0,0.0,np.pi/4.0,0.0,0.0,0.0,1014.0,0.0,0.0,0.5)
print(aob.shape)

iy, im, id, ihmsf = erfa.d2dtf("UTC", 3, jd, 0.0)
print(iy.shape, ihmsf.shape, ihmsf.dtype)
print(ihmsf)

iy, im, id, ihmsf = erfa.d2dtf("UTC", 3, jd[0], 0.0)
print(iy.shape, ihmsf.shape, ihmsf.dtype)
print(ihmsf)

