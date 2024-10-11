import os # pragma: no cover

os = type('Mock', (object,), {'environ': {'GCS_PROJECT_ID': 'your-project-id'}})() # pragma: no cover
bucket = type('Mock', (object,), {'get_blob': lambda x: type('Mock', (object,), {'download_as_string': lambda: b'dummy-content', 'acl': []})()})() # pragma: no cover
path = 'dummy/path' # pragma: no cover

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
