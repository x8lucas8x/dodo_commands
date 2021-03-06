.. _installation:

************
Installation
************

Step 1: Install prerequisites
==========================================

Dodo Commands depends on the python-virtualenv package.
In addition, some of the Dodo commands use git.

.. code-block:: bash

    sudo apt-get install python-virtualenv git


Step 2: Install
===============

.. code-block:: bash

    pip install dodo_commands

Once installed, you can upgrade the dodo_commands python package with

.. code-block:: bash

    dodo upgrade


Step 3: Install some default commands
=====================================

At this point, the Dodo Commands framework is installed but it will not contain any commands you can run. To install the standard Dodo Commands, run:

.. code-block:: bash

    dodo install-default-commands standard_commands

The :code:`standard_commands` directory was found "magically" because it comes with the Dodo Commands python package. Commands are installed in the ``~/.dodo_commands/default_commands`` directory. To read more about installing default commands, see :ref:`commands`.

.. tip::

   On Mac you may need to create a file ``~/.distutils.cfg`` that `sets an empty prefix <http://stackoverflow.com/a/24357384/301034>`_ to prevent errors stating "must supply either home or prefix/exec-prefix -- not both".


Step 4: (Optional) Create aliases
=================================

NOTE: this step is only necessary if you installed :code:`dodo_commands`
into a virtual environment.

To make sure that the :code:`dodo` command is always found,
call :code:`which dodo` and add the resulting path (the directory part) to the PATH in
in your :code:`~/.bashrc`. The result should look something like this:

.. code-block:: bash

    export PATH=$PATH:/home/maarten/projects/dodo_commands_env/bin


Step 5: (Optional) Activate the latest project automatically
============================================================

To automatically activate the last used Dodo Commands project, add this line to your :code:`~/.bashrc` file:

.. code-block:: bash

    $(dodo activate --latest)

If you wish to be able to toggle the automatic activation on and off, read about :ref:`autostart`.

Step 6: (Optional) Tweak global configuration
=============================================

The first time you call :code:`dodo`, a global :code:`~/.dodo_commands/config` file is created (unless it already exists) with the following settings:

- :code:`projects_dir` is the location where your projects are stored (defaults to :code:`~/projects`)

- :code:`python` is the python interpreter that is used in the virtualenv of your projects (defaults to :code:`python`). If your OS uses Python 2 by default then you may want to set this to :code:`python3` to use the latest python.

- :code:`diff_tool` is the diff tool used to show changes to your project configuration files. It's recommended to install and use :code:`meld` for this option.
