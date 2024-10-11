import hashlib # pragma: no cover
from urllib.parse import urlparse # pragma: no cover
class MockRequest: pass # pragma: no cover

def to_bytes(url): return url.encode('utf-8') # pragma: no cover
request = type('MockRequest', (object,), {'url': 'http://example.com/image'})() # pragma: no cover
thumb_id = 'example_thumb_id' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/images.py
from l3.Runtime import _l_
thumb_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
_l_(9138)
aux = f'thumbs/{thumb_id}/{thumb_guid}.jpg'
_l_(9139)
exit(aux)
