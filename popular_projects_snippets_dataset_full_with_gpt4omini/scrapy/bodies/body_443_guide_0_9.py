import os # pragma: no cover

os.environ['GCS_PROJECT_ID'] = 'your_project_id' # pragma: no cover
bucket = 'your_bucket_name' # pragma: no cover
path = 'your_blob_path' # pragma: no cover
class MockACL: __getitem__ = lambda self, x: x; __iter__ = lambda self: iter([]); # pragma: no cover
blob = type('MockBlob', (object,), {'download_as_string': lambda self: b'test content', 'acl': MockACL(), 'delete': lambda self: None})() # pragma: no cover
client = type('MockClient', (object,), {'get_bucket': lambda self, name: type('MockBucket', (object,), {'get_blob': lambda self, path: blob, 'delete_blob': lambda self, path: None})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
from l3.Runtime import _l_
try:
    from google.cloud import storage
    _l_(5122)

except ImportError:
    pass
client = storage.Client(project=os.environ.get('GCS_PROJECT_ID'))
_l_(5123)
bucket = client.get_bucket(bucket)
_l_(5124)
blob = bucket.get_blob(path)
_l_(5125)
content = blob.download_as_string()
_l_(5126)
acl = list(blob.acl)  # loads acl before it will be deleted
_l_(5127)  # loads acl before it will be deleted
bucket.delete_blob(path)
_l_(5128)
aux = (content, acl, blob)
_l_(5129)
exit(aux)
