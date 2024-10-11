import os # pragma: no cover

class MockBlob:  # Mock implementation of blob # pragma: no cover
    def download_as_string(self): # pragma: no cover
        return b'blob content' # pragma: no cover
    @property # pragma: no cover
    def acl(self): # pragma: no cover
        return [] # pragma: no cover
    def delete(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockBucket:  # Mock implementation of bucket # pragma: no cover
    def get_blob(self, path): # pragma: no cover
        return MockBlob() # pragma: no cover
    def delete_blob(self, path): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class MockClient:  # Mock implementation of client # pragma: no cover
    def bucket(self, name): # pragma: no cover
        return MockBucket() # pragma: no cover
 # pragma: no cover
os.environ['GCS_PROJECT_ID'] = 'mock_project_id' # pragma: no cover
client = MockClient() # pragma: no cover
bucket = client.bucket('mock_bucket') # pragma: no cover
path = 'mock/path/to/blob' # pragma: no cover

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
