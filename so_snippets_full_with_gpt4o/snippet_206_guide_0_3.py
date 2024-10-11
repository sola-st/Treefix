import os # pragma: no cover
import shutil # pragma: no cover
import requests # pragma: no cover

class MockWget: # pragma: no cover
    @staticmethod # pragma: no cover
    def download(path, urls, filenames=None, extract=False): # pragma: no cover
        if not os.path.exists(path): # pragma: no cover
            os.makedirs(path) # pragma: no cover
        if isinstance(urls, str): # pragma: no cover
            urls = [urls] # pragma: no cover
        for url in urls: # pragma: no cover
            filename = os.path.join(path, os.path.basename(url) if filenames is None else filenames) # pragma: no cover
            with open(filename, 'wb') as f: # pragma: no cover
                f.write(requests.get(url).content) # pragma: no cover
            if extract and filename.endswith('.zip'): # pragma: no cover
                shutil.unpack_archive(filename, path) # pragma: no cover
mock_wget = type('Mock', (object,), dict(wget=MockWget)) # pragma: no cover
wget = mock_wget.wget # pragma: no cover

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

