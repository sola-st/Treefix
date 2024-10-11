# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4888027/python-and-pip-list-all-versions-of-a-package-thats-available
from l3.Runtime import _l_
try:
    import requests
    _l_(14954)

except ImportError:
    pass
r = requests.get("https://pypi.org/pypi/Flask/json")
_l_(14955)
print(r.json()['releases'].keys())
_l_(14956)

dict_keys(['0.1', '0.10', '0.10.1', '0.11', '0.11.1', '0.12', '0.12.1', '0.12.2', '0.12.3', '0.12.4', '0.2', '0.3', '0.3.1', '0.4', '0.5', '0.5.1', '0.5.2', '0.6', '0.6.1', '0.7', '0.7.1', '0.7.2', '0.8', '0.8.1', '0.9', '1.0', '1.0.1', '1.0.2'])
_l_(14957)

