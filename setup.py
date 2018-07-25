from setuptools import setup

setup(name='dircheck',
      version='0.1',
      description='Prints the 5 biggest directories with size',
      url='',
      author='Taylor Dudley',
      packages=['dircheck'],
      install_requires=[
            'os',
            'systems',
            'heapq',
            'psutil'
      ],
      zip_safe=False)