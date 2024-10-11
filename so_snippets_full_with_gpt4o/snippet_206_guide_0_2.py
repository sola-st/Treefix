import os # pragma: no cover

MockWget = type('MockWget', (object,), {'download': lambda *args, **kwargs: print('Simulated download with args:', args, 'and kwargs:', kwargs)}) # pragma: no cover
wget = MockWget() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/22676/how-to-download-a-file-over-http
from l3.Runtime import _l_
try:
    from parallel_sync import wget
    _l_(15272)

except ImportError:
    pass
urls = ['http://something.png', 'http://somthing.tar.gz', 'http://somthing.zip']
_l_(15273)
wget.download('/tmp', urls)
_l_(15274)
# or a single file:
wget.download('/tmp', urls[0], filenames='x.zip', extract=True)
_l_(15275)

