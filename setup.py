from setuptools import setup
import os
import sys


# in setup.py
if 'bdist_wheel' in sys.argv:
    raise RuntimeError("This setup.py does not support wheels")

setup(name='dodo_commands',
      version='0.3.4',
      description='Project-aware development environments, inspired by django-manage',
      url='https://github.com/mnieber/dodo_commands',
      download_url='https://github.com/mnieber/dodo_commands/tarball/0.3.4',
      author='Maarten Nieber',
      author_email='hallomaarten@yahoo.com',
      license='MIT',
      packages=[
          'dodo_commands',
          'dodo_commands.framework',
      ],
      package_data={
          'dodo_commands': [
              'extra/__init__.py',
              'extra/git_commands/*.py',
              'extra/git_commands/*.meta',
              'extra/standard_commands/*.py',
              'extra/standard_commands/*.meta',
              'extra/standard_commands/decorators/*.py',
              'extra/webdev_commands/*.py',
              'extra/webdev_commands/*.meta',
          ]
      },
      data_files=[
          (os.path.expanduser('~/.dodo_commands'), ['res/config']),
          (os.path.expanduser('~/.dodo_commands/default_commands'), ['res/default_commands/__init__.py']),
      ],
      entry_points={
          'console_scripts': [
              'dodo-activate=dodo_commands.dodo_activate:main',
              'dodo-install-default-commands=dodo_commands.dodo_install_commands:main',
          ]
      },
      install_requires=[
          'argcomplete',
          'plumbum',
          'PyYaml',
          'six',
      ],
      zip_safe=False)
