import os # pragma: no cover

import os # pragma: no cover

os.environ['GCS_PROJECT_ID'] = 'mock-gcs-project-id' # pragma: no cover
bucket = type('MockBucket', (object,), {'get_blob': lambda self, path: type('MockBlob', (object,), {'download_as_string': lambda s: b'sample content', 'acl': [], 'delete': lambda s: None})(), 'delete_blob': lambda s, path: None})() # pragma: no cover
path = 'path/to/mock/blob.txt' # pragma: no cover
client = type('MockClient', (object,), {'get_bucket': lambda s, bucket_name: bucket})() # pragma: no cover

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
