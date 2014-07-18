from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

cython_numpy_ext = Extension("erfa.cython_numpy",
                             ["cython_numpy/erfa.pyx"],
                             libraries=['erfa'], 
                             include_dirs = [np.get_include(), '/opt/local/include'],
                             library_dirs = ['/opt/local/lib'])

setup(name = "erfa",
      cmdclass = { "build_ext": build_ext },
      packages = ["erfa"],
      package_dir = {"erfa":"."},
      ext_modules = [cython_numpy_ext])
