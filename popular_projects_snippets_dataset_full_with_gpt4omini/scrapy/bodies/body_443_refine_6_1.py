import os # pragma: no cover

os.environ['GCS_PROJECT_ID'] = 'your_project_id' # pragma: no cover
path = 'your/file/path.txt' # pragma: no cover

import os # pragma: no cover
from unittest.mock import Mock # pragma: no cover

os.environ['GCS_PROJECT_ID'] = 'your_project_id' # pragma: no cover
client = Mock() # pragma: no cover
mock_blob = Mock() # pragma: no cover
mock_blob.download_as_string.return_value = b'content' # pragma: no cover
mock_blob.acl = [] # pragma: no cover
client.bucket = Mock(return_value=Mock(get_blob=Mock(return_value=mock_blob), delete_blob=Mock())) # pragma: no cover
bucket = client.bucket('your_bucket_name') # pragma: no cover
path = 'your/file/path.txt' # pragma: no cover

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
