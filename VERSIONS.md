# Version history

## 0.8.0

- Add optional --project-name to diff command
- Fix the tests, remove the installation test
- Refactor ConfigIO and CommandPath

## 0.7.8

- Replace PyYAML with ruamel.yaml
- Add flag --sudo to dodo upgrade
- Mark commands that do not honor --confirm and --echo as unsafe
- Use /DOCKER/link_list to link containers in docker decorator

## 0.7.7

- Handle case where pip is located inside /usr/local instead of /usr

## 0.7.6

- Print clearer warning in check-version and check-config-version
- Fix broken reference to get_version

## 0.7.5

- Fix crash in install-default-commands when no pip packages are specified

## 0.7.4

- Fix importing missing dependencies via the meta file
- Obtain version with dodo --version
- Move git_commands and webdev_commands to external git repos
- Allow to install pip packages in install-default-commands
- Prevent running dodo upgrade with activated dodo project
- Fix crash in dodo activate when no project is specified

## 0.7.3

- Fix setup.py

## 0.7.2

- Fix setup.py

## 0.7.1

- Write sorted dicts to dodo configuration files

## 0.7.0

- Use a system `dodo` entry point

## 0.6.3

- Replace config-get command by dodo print-config --key
- Use tape instead of tape-run again in tape command
- Add --watch argument to webpack command

## 0.6.2

- Fix remaining broken import

## 0.6.1

- Fix dodo-upgrade (nothing was executed)

## 0.6.0

- Print warning for unexpanded config keys

## 0.5.2

- Fix broken imports

## 0.5.1

- Add check-version command

## 0.5.0

- Improve formatting of errors in the console output
- Add tape command

## 0.4.7

- Add dodo-upgrade command to upgrade dodo_commands itself
- Remove obsolete commands

## 0.4.6

- Fix of error in 0.4.5 (node-sass command)

## 0.4.5

- Small fixes in node-sass and django-manage commands

## 0.4.4

- Improve documentation
- Add node-sass command
- Rename --docker_image to --image in dodo dockerbuild

## 0.4.3

- Remove hack in dodo runpostgres command

## 0.4.2

- Fix crash when latest_project value is missing in global config

## 0.4.1

- Also use DOCKER/volumes_from_list in docker decorator
- Use standard docker container names in webpack, autoless and pytest

## 0.4.0

- Commands can use decorated.docker_options to add more docker options
- Remove port argument from docker decorator
- Link pg docker container in django-manage command

## 0.3.10

- Require option --force or --confirm in bootstrap command
- Add pytest_args argument to pytest command

## 0.3.9

- Fix: broken paths

## 0.3.8

- Fix: avoid permission problems by not installing config file during setup
- Add option --latest to dodo-activate

## 0.3.7

- Fix problem with dodo diff <somefile>
- Change --command option in "docker" to a positional argument

## 0.3.6

- Remove git-gui command (use dodo git gui instead)
- Simplify the cd and which commands
- Print an error if config layer filename not found

## 0.3.5

- Update documentation

## 0.3.4

- Fix PyPI installation problem

## 0.3.3

- Fix: ensure less output directory exists in autoless command
- Make the git command generic

## 0.3.1

- Fix: resolve references in command_path

## 0.3.0

- BREAKING: symlink dodo_commands in the site-packages of the dodo project
- BREAKING: remove framework and default_commands dirs from dodo project dir

## 0.2.3

- Simplify django-manage command and make it work for Python 2

## 0.2.2

- Add argument --port to docker decorator

## 0.2.1

- Fix: Don't crash on non-standard filenames in /ROOT/layers
- Add optional argument --command to "dodo docker"
- Add argument --res to cd and which commands

## 0.2.0

- BREAKING: Use pip to install dodo_commands
- BREAKING: Many small changes in api

## 0.1.6

- FIX: Remove stray pudb invocation in bootstrap command
- Small improvements in commands: django-manage, autoless
- Also disable docker if /DOCKER/enabled equals "False"

## 0.1.5

- New command chown-src
- Better error reporting in gitsplit command
- Configurable python interpreter in django-manage command
- Make directories in ${DOCKER/extra_dirs} available in dockerbuild command
- Use ${/DOCKER/default_cwd} in docker command
- Add argument 'branch' to bootstrap command

## 0.1.4

- Allow to create a project in an existing directory if no dodo_commands directory exists

## 0.1.3

- FIX: Allow storing CommandPaths in configuration layers.
- FIX: Use symlink dodo_commands/defaults/project in diff command

## 0.1.2

- BREAKING: Store env inside dodo_commands, and config.yaml in dodo_commands/res
- FIX: Fix layer and print-config, update README.md to explain configuration layers

## 0.1.1

- FIX: Added documentation and fixed broken references to defaults/commands
- NEW: Argument --create-from to dodo_activate

## 0.1.0

- BREAKING: Renamed option projects_folder to projects_dir in dodo_commands.config.
- BREAKING: Added option python_interpreter (default=python) to dodo_commands.config. This option sets the python interpreter that is used in the project's virtualenv.
- FIX: Changed version back from 1.0.0 to 0.1.0 to indicate beta status
- FIX: Several other fixes
- NEW: Commands new-command, git-gui, gitk, gitsplit, git, config-get, bootstrap
