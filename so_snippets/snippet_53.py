# Extracted from https://stackoverflow.com/questions/2720014/how-to-upgrade-all-python-packages-with-pip
pip list --format freeze --outdated | sed 's/(.*//g' | xargs -n1 pip install -U

pip list --format freeze --outdated | sed 's/=.*//g' | sed 's/^<First characters of the first error>.*//' | sed 's/^<First characters of the second error>.*//' | xargs pip install -U

