#pyenv install python if needed
pyenv env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install {{cookiecutter.python_version}}
#pyenv local this python version
pyenv local {{cookiecutter.python_version}}
#pyenv virtulaenv make environemnt
pyenv virtualenv  {{cookiecutter.python_version}} {{cookiecutter.project_name}}
#activate the environment
pyenv activate {{cookiecutter.project_name}}
#in new environment, pip install reqiurements
pip install -r requirements.txt