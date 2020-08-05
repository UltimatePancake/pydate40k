from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='pydate40k',
      version='0.1',
      url='https://github.com/UltimatePancake/pydate40k',
      license='WTFPL',
      author='Pier Gaetani',
      author_email='pier.gaetani@gmail.com',
      description='Return a date in the format of the Imperial Calendar',
      packages=find_packages(exclude=['tests']),
      long_description=long_description,
      long_description_content_type='text/markdown',
      python_requires='>=3.7',
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      zip_safe=False)
