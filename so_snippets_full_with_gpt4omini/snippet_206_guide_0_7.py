import os # pragma: no cover
import shutil # pragma: no cover

urls = ['http://something.png', 'http://somthing.tar.gz', 'http://somthing.zip'] # pragma: no cover
class MockWget:# pragma: no cover
    def download(self, directory, urls, filenames=None, extract=False):# pragma: no cover
        for url in urls:# pragma: no cover
            print(f'Downloading {url} to {directory}/{filenames if filenames else os.path.basename(url)}')# pragma: no cover
            # Mock download functionality# pragma: no cover
            if extract:# pragma: no cover
                print(f'Extracting {directory}/{filenames if filenames else os.path.basename(url)}')# pragma: no cover
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

