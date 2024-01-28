__version__ = "2.1.0"

from setuptools import setup
import sys
sys.path.insert(0, ".")

setup(
    name='WeightedCorr',
    version=__version__,
    author='Matthijs van der Zee',
    setup_requires=["numpy",'pandas', 'scipy','wheel'],
    build_requires=["numpy",'pandas', 'scipy','wheel'],
    py_modules=['WeightedCorr'], 
    install_requires=['numpy', 'pandas', 'scipy','wheel'],
)
