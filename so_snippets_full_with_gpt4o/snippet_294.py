# Extracted from https://stackoverflow.com/questions/15221473/how-do-i-update-upgrade-pip-itself-from-inside-my-virtual-environment
python -c "import urllib.request; exec(urllib.request.urlopen('https://bootstrap.pypa.io/get-pip.py').read())"

python -c "import urllib2; exec(urllib2.urlopen('https://bootstrap.pypa.io/get-pip.py').read())"

