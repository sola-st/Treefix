import os # pragma: no cover

class MockWget(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def download(directory, urls, filenames=None, extract=False): # pragma: no cover
        os.makedirs(directory, exist_ok=True) # pragma: no cover
        print(f"Downloading {urls} to {directory}") # pragma: no cover
        if extract: # pragma: no cover
            print(f"Extracting {filenames} in {directory}") # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
wget = MockWget() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/22676/how-to-download-a-file-over-http
from l3.Runtime import _l_
try:
    from parallel_sync import wget
    _l_(3216)

except ImportError:
    pass
urls = ['http://something.png', 'http://somthing.tar.gz', 'http://somthing.zip']
_l_(3217)
wget.download('/tmp', urls)
_l_(3218)
# or a single file:
wget.download('/tmp', urls[0], filenames='x.zip', extract=True)
_l_(3219)

