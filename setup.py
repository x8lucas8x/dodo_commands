from setuptools import setup
import os


setup(name='dodo_commands',
      version='0.2.0',
      description='Project-aware development environments, inspired by django-manage',
      url='https://github.com/mnieber/dodo_commands',
      author='Maarten Nieber',
      author_email='hallomaarten@yahoo.com',
      license='MIT',
      packages=[
          'dodo_commands',
          'dodo_commands.framework',
      ],
      package_data={
          'dodo_commands': [
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