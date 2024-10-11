import os # pragma: no cover
import sys # pragma: no cover

class MockWget: # pragma: no cover
    @staticmethod # pragma: no cover
    def download(destination, urls, filenames=None, extract=False): # pragma: no cover
        print(f'Downloading {urls} to {destination}') # pragma: no cover
        if filenames: # pragma: no cover
            print(f'Filenames: {filenames}') # pragma: no cover
        if extract: # pragma: no cover
            print('Extracting files') # pragma: no cover

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

