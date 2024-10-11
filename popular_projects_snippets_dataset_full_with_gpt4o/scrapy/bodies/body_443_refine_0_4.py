import os # pragma: no cover

os.environ = {'GCS_PROJECT_ID': 'your-gcs-project-id'} # pragma: no cover
bucket = type('MockBucket', (object,), {'get_blob': lambda self, x: type('MockBlob', (object,), {'download_as_string': lambda self: b'Test Content', 'acl': type('MockACL', (object,), {}), 'delete_blob': lambda self, y: None})()})() # pragma: no cover
path = 'path/to/blob' # pragma: no cover

import os # pragma: no cover
from unittest.mock import Mock # pragma: no cover

os.environ = {'GCS_PROJECT_ID': 'your-gcs-project-id'} # pragma: no cover
mock_blob = Mock() # pragma: no cover
mock_blob.download_as_string.return_value = b'Test Content' # pragma: no cover
mock_blob.acl = ['READER', 'WRITER'] # pragma: no cover
bucket = Mock() # pragma: no cover
bucket.get_blob.return_value = mock_blob # pragma: no cover
path = 'path/to/blob' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
from l3.Runtime import _l_
try:
    from google.cloud import storage
    _l_(16778)

except ImportError:
    pass
client = storage.Client(project=os.environ.get('GCS_PROJECT_ID'))
_l_(16779)
bucket = client.get_bucket(bucket)
_l_(16780)
blob = bucket.get_blob(path)
_l_(16781)
content = blob.download_as_string()
_l_(16782)
acl = list(blob.acl)  # loads acl before it will be deleted
_l_(16783)  # loads acl before it will be deleted
bucket.delete_blob(path)
_l_(16784)
aux = (content, acl, blob)
_l_(16785)
exit(aux)
