headers = {'Content-Type': 'text/plain'} # pragma: no cover

headers = {'Content-Type': 'text/plain'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
from l3.Runtime import _l_
if headers and 'Content-Type' in headers:
    _l_(21032)

    aux = headers['Content-Type']
    _l_(21031)
    exit(aux)
aux = 'application/octet-stream'
_l_(21033)
exit(aux)
