import os # pragma: no cover

class MockWget: # pragma: no cover
    def download(self, directory, urls, filenames=None, extract=False): # pragma: no cover
        if not os.path.exists(directory): # pragma: no cover
            os.makedirs(directory) # pragma: no cover
        if isinstance(urls, str): # pragma: no cover
            urls = [urls] # pragma: no cover
        for url in urls: # pragma: no cover
            local_filename = filenames if filenames else os.path.basename(url) # pragma: no cover
            print(f'Downloading {url} to {directory}/{local_filename}') # pragma: no cover
            if extract: # pragma: no cover
                print(f'Extracting {local_filename} in {directory}') # pragma: no cover
urls = ['http://something.png', 'http://somthing.tar.gz', 'http://somthing.zip'] # pragma: no cover
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

