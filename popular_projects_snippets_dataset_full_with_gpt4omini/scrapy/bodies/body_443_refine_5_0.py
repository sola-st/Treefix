import os # pragma: no cover

os.environ['GCS_PROJECT_ID'] = 'your-project-id' # pragma: no cover
path = 'path/to/your/file.txt' # pragma: no cover
type('MockBlob', (object,), {'download_as_string': lambda s: b'file content', 'acl': [], 'delete': lambda s: None}) # pragma: no cover
type('MockBucket', (object,), {'get_blob': lambda s, p: MockBlob(), 'delete_blob': lambda s, p: None}) # pragma: no cover

class MockBlob:# pragma: no cover
    def download_as_string(self):# pragma: no cover
        return b'file content'# pragma: no cover
    @property# pragma: no cover
    def acl(self):# pragma: no cover
        return []# pragma: no cover
    def delete(self):# pragma: no cover
        pass # pragma: no cover
class MockBucket:# pragma: no cover
    def get_blob(self, path):# pragma: no cover
        return MockBlob()# pragma: no cover
    def delete_blob(self, path):# pragma: no cover
        pass # pragma: no cover
class MockClient:# pragma: no cover
    def bucket(self, bucket_name):# pragma: no cover
        return MockBucket() # pragma: no cover
os.environ['GCS_PROJECT_ID'] = 'your-project-id' # pragma: no cover
client = MockClient() # pragma: no cover
bucket = client.bucket('your-bucket-name') # pragma: no cover
path = 'path/to/your/file.txt' # pragma: no cover

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
