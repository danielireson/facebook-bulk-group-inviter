from setuptools import setup

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
  name = 'facebook-bulk-group-inviter',
  version = '0.0.1',
  packages = ['cli'],
  install_requires=requirements,
  entry_points = {
    'console_scripts': [
      'facebook-bulk-group-inviter = cli.__main__:main'
    ]
  })
