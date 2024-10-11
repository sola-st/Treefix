import os # pragma: no cover
from types import SimpleNamespace # pragma: no cover

class MockWget: # pragma: no cover
    @staticmethod # pragma: no cover
    def download(path, urls, filenames=None, extract=False): # pragma: no cover
        print(f"Downloading {urls} to {path} with filenames={filenames} and extract={extract}") # pragma: no cover
wget = SimpleNamespace(download=MockWget.download) # pragma: no cover
parallel_sync = SimpleNamespace(wget=wget) # pragma: no cover
sys.modules['parallel_sync'] = parallel_sync # pragma: no cover

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

