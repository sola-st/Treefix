# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
from l3.Runtime import _l_
try:
    import requests
    _l_(12239)

except ImportError:
    pass

url = 'https://www.python.org/static/img/python-logo.png'
_l_(12240)
fileName = 'D:\Python\dwnldPythonLogo.png'
_l_(12241)
req = requests.get(url)
_l_(12242)
file = open(fileName, 'wb')
_l_(12243)
for chunk in req.iter_content(100000):
    _l_(12245)

    file.write(chunk)
    _l_(12244)
file.close()
_l_(12246)

