from setuptools import setup

setup(
  name = 'facebook-bulk-group-inviter',
  version = '0.0.1',
  packages = ['cli'],
  entry_points = {
    'console_scripts': [
      'facebook-bulk-group-inviter = cli.__main__:main'
    ]
  })
