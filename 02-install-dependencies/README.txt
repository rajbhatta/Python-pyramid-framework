Install_Package_02
==================

Getting Started
---------------

- Change directory into your newly created project if not already there. Your
  current directory should be the same as this README.txt file and setup.py.

    cd Install_Package_02

- Create a Python virtual environment, if not already created.

    python3 -m venv package

- Upgrade packaging tools, if necessary.

    package/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    package/bin/pip install -e ".[testing]"

- Run your project's tests.

    package/bin/pytest

- Run your project.

    package/bin/pserve development.ini
