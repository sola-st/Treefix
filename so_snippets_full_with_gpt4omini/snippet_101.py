# Extracted from https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x
mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew

sudo nano  ~/.bash_profile

export PATH="$HOME/homebrew/bin:$PATH"

brew install python

sudo nano  ~/.bash_profile

alias pip=pip3

brew install python

brew install python3

brew install python3

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

pip -V
python --version

pip3 -V
python3 --version

deactivate

