import os # pragma: no cover

import os # pragma: no cover
from unittest.mock import Mock # pragma: no cover

os.environ['GCS_PROJECT_ID'] = 'my-gcs-project-id' # pragma: no cover
bucket = Mock() # pragma: no cover
bucket.get_blob = Mock(return_value=Mock(download_as_string=Mock(return_value=b'file content'), acl=[], delete=Mock())) # pragma: no cover
bucket.delete_blob = Mock() # pragma: no cover
path = 'path/to/my/blob' # pragma: no cover

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
