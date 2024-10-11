# Extracted from https://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install
virtualenv env
source env/bin/activate

pip install flask

pip freeze > requirements.txt

pip install -r requirements.txt

