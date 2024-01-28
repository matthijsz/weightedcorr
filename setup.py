from setuptools import setup
import sys
sys.path.insert(0, ".")
from WeightedCorr import __version__

setup(
    name='WeightedCorr',
    version=__version__,
    author='Matthijs van der Zee',
    setup_requires=["numpy"],
    build_requires=["numpy"],
    py_modules=['WeightedCorr'], 
    install_requires=['numpy', 'pandas', 'scipy'],
)
