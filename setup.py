from setuptools import setup
from biketrauma_nmd import __version__ as current_version

setup(
  name='biketrauma_nmd',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='http://github.com/AyoubAarab/python_module_tp.git',
  author='Ayoub Aarab',
  author_email='ayoub.aarab.work@gmail.com',
  license='MIT',
  packages=['biketrauma_nmd','biketrauma_nmd.io', 'biketrauma_nmd.preprocess', 'biketrauma_nmd.vis'],
  zip_safe=False
)