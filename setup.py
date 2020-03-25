from setuptools import setup, Extension
from Cython.Distutils import build_ext

import os
import Cython
import numpy
from io import open

extensions = [
    Extension("GasUtil",["PyGasMix/GasUtil.pyx","PyGasMix/Gases/GasUtil.pxd"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("Gasmix",["PyGasMix/Gasmix.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("ARGON",["PyGasMix/Gases/ARGON.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("CF4",["PyGasMix/Gases/CF4.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("CH4",["PyGasMix/Gases/CH4.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("CO2",["PyGasMix/Gases/CO2.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("DEUTERIUM",["PyGasMix/Gases/DEUTERIUM.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("DME",["PyGasMix/Gases/DME.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("ETHANE",["PyGasMix/Gases/ETHANE.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("H2O",["PyGasMix/Gases/H2O.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("HELIUM3",["PyGasMix/Gases/HELIUM3.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("HELIUM4",["PyGasMix/Gases/HELIUM4.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("HYDROGEN",["PyGasMix/Gases/HYDROGEN.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("ISOBUTANE",["PyGasMix/Gases/ISOBUTANE.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("KRYPTON",["PyGasMix/Gases/KRYPTON.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("NEON",["PyGasMix/Gases/NEON.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("NITROGEN",["PyGasMix/Gases/NITROGEN.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("OXYGEN",["PyGasMix/Gases/OXYGEN.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("PROPANE",["PyGasMix/Gases/PROPANE.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("XENON",["PyGasMix/Gases/XENON.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),
    Extension("XENONMERT",["PyGasMix/Gases/XENONMERT.pyx"],include_dirs=[numpy.get_include(),os.getcwd()+'/PyGasMix/'],extra_compile_args = ["--inplace"]),

]
setup(
    setup_requires=[
        'cython>=0.2',
    ],
    zip_safe=False,
    name='PyGasMix',  # Required
    packages=['PyGasMix','PyGasMix/Gases'],

    version='1.0.0',  # Required
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    package_dir={'PyGasMix': 'PyGasMix'},
    install_requires=['numpy==1.16.1','cython'],  # Optional
    package_data={  # Optional
        'PyGasMix': ['./PyGasMix/*.pxd'],
        'PyGasMix/Gases':['./PyGasMix/Gases/gases.npy','./PyGasMix/Gases/*.pxd','./PyGasMix/*.pxd']
    },
    ext_modules = extensions,
    cmdclass={'build_ext': build_ext},
)