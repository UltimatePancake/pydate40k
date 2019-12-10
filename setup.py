from setuptools import setup, find_packages

setup(name='pydate40k',
      version='0.1',
      url='https://github.com/UltimatePancake/pydate40k',
      license='MIT',
      author='Pier Gaetani',
      author_email='pier.gaetani@gmail.com',
      description='Return a date in the format of the Imperial Calendar',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
