PYTHON=.venv/bin/python # path to pyphon
PIP=.venv/bin/pip # path to pip
SOURCE_VENV=. .venv/bin/activate


install:
    virtualenv .venv
    $(SOURCE_VENV) && $(PIP) install -e PACKAGE
    $(SOURCE_VENV) && $(PIP) install -r requirements.txt 
