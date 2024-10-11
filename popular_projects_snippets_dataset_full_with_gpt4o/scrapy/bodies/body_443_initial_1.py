import os # pragma: no cover

os = type('MockOS', (object,), {'environ': {'GCS_PROJECT_ID': 'your-gcs-project-id'}}) # pragma: no cover
bucket = type('MockBucket', (object,), {'get_blob': lambda self, path: MockBlob(), 'delete_blob': lambda self, path: None})() # pragma: no cover
path = 'your/path/here' # pragma: no cover
class MockBlob(object): # pragma: no cover
    def download_as_string(self): # pragma: no cover
        return b'some-blob-content' # pragma: no cover
    @property # pragma: no cover
    def acl(self): # pragma: no cover
        return ['ACL_ENTRY_1', 'ACL_ENTRY_2'] # pragma: no cover

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
