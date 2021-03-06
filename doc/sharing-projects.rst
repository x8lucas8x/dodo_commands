.. _sharing_projects:

****************
Sharing projects
****************

Objectives
==========

If someone wants to join your project, then it makes sense to share your working environment with them. At the same time, you want your working environment to be independent, so that you can arrange it to your preferences.
In the explanation below, we'll assume that you have the following project directory layout:

.. code-block:: bash

    ~/projects/FooBar                    # root of the project
    ~/projects/FooBar/src                # cloned https://github.com/foo/foobar.git repository
    ~/projects/FooBar/dodo_commands/res  # your Dodo Commands configuration files

Bootstrapping
=============

The proposed solution to the above problem is the following:

- you add *default* Dodo Commands configuration files at location ``~/projects/FooBar/src/extra/dodo_commands/res`` and commit this to your git repository.

- your colleague starts out by creating an empty Dodo Commands project using ``dodo activate FooBar --create``.

Your colleague then calls the ``bootstrap`` command to clone the project repository and initialize their Dodo Commands configuration with a *copy* of the default configuration files:

.. code-block:: bash

    dodo bootstrap src extra/dodo_commands/res --force --git-url https://github.com/foo/foobar.git

In the above example, the repository is cloned to the ``src`` subdirectory of the project directory. After cloning, all default configuration files are copied from the ``extra/dodo_commands/res`` location (which is relative to the root of the cloned repository) to ``~/projects/FooBar/dodo_commands/res``. Finally, the location of the cloned sources (``src``) is stored in the configuration under the ``${/ROOT/src_dir}`` key.

At this point, your colleague has the same directory structure as you, with one additional symlink:

.. code-block:: bash

    ~/projects/FooBar                                # root of the project
    ~/projects/FooBar/src                            # cloned https://github.com/foo/foobar.git repository
    ~/projects/FooBar/src/extra/dodo_commands/res    # default Dodo Commands configuration files
    ~/projects/FooBar/dodo_commands/res              # local copies of the default Dodo Commands configuration files
    ~/projects/FooBar/dodo_commands/default_project  # symlink to ~/projects/FooBar/src/extra/dodo_commands/res

- the additional symlink is used by the ``dodo diff`` command to show the differences between your local configuration files and the default files. Your colleague can freely change their local configuration files and use `dodo diff .` to update the default files and push them.

- we recommend to set :code:`meld` as the ``diff_tool`` in :code:`~/.dodo_commands/config`.

- if you call ``dodo bootstrap`` with ``--confirm`` but without the ``--git-url`` argument, then it doesn't clone the git repository but only creates the symlink (when it asks to copy configuration files, answer 'no') :

.. code-block:: bash

    dodo bootstrap src extra/dodo_commands/res --confirm

- To synchronize only config.yaml, call ``dodo diff config.yaml``. It's a good practice to use the value ``${/ROOT/version}`` to track whether the copied configuration is up-to-date or not.


Bootstrapping with monolithic repositories
==========================================

A monolithic repository may contain several projects that each have their own Dodo Commands configuration. In this scenario, several Dodo Commands projects should share the same source tree:

.. code-block:: bash

    # Get monolithic repository.

    cd ~/sources
    git clone https://github.com/foo/monolith.git

    # Bootstrap the foobar project without cloning the sources.
    # Copy configuration from ~/sources/monolith/foobar/extra/dodo_commands/res

    $(dodo activate --create foobar)
    dodo bootstrap ~/sources/monolith/foobar extra/dodo_commands/res --force


Checking the config version
===========================

The ``dodo check-config-version`` command compares the ``${/ROOT/version}`` value in your local configuration with the value in the (shared) default configuration. If someone bumped the version in the shared configuration, it will tell you that your local configuration is not up-to-date (in that case, use ``dodo diff .`` to synchronize).
One of the values that you synchronize with ``dodo diff .`` is ``${/ROOT/required_dodo_commands_version}``. The ``dodo check-version`` command reads this value and warns you if your Dodo Commands version is too old (if it is, then you can run ``dodo upgrade`` to upgrade Dodo Commands). The small script written by ``dodo autostart on`` (see :ref:`autostart`) calls both checks, and this helps you to stay synchronized.
