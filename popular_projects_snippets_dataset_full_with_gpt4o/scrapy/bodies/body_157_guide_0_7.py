import botocore.session # pragma: no cover
from typing import Tuple, Type # pragma: no cover

class Mock: # pragma: no cover
    AWS_ACCESS_KEY_ID = 'your_access_key_id' # pragma: no cover
    AWS_SECRET_ACCESS_KEY = 'your_secret_access_key' # pragma: no cover
    AWS_SESSION_TOKEN = 'your_session_token' # pragma: no cover
    AWS_ENDPOINT_URL = 'http://localhost:4566' # pragma: no cover
    AWS_REGION_NAME = 'us-east-1' # pragma: no cover
    AWS_USE_SSL = False # pragma: no cover
    AWS_VERIFY = False # pragma: no cover
    @staticmethod # pragma: no cover
    def is_botocore_available() -> bool: # pragma: no cover
        try: # pragma: no cover
            return True # pragma: no cover
        except ImportError: # pragma: no cover
            return False # pragma: no cover
    @staticmethod # pragma: no cover
    def NotConfigured(message: str): # pragma: no cover
        raise Exception(message) # pragma: no cover
self = type('Mock', (object,), dict(is_botocore_available=Mock.is_botocore_available, NotConfigured=Mock.NotConfigured, AWS_ACCESS_KEY_ID=Mock.AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY=Mock.AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN=Mock.AWS_SESSION_TOKEN, AWS_ENDPOINT_URL=Mock.AWS_ENDPOINT_URL, AWS_REGION_NAME=Mock.AWS_REGION_NAME, AWS_USE_SSL=Mock.AWS_USE_SSL, AWS_VERIFY=Mock.AWS_VERIFY))() # pragma: no cover
uri = 's3://mybucket/myprefix' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
from l3.Runtime import _l_
if not is_botocore_available():
    _l_(20932)

    raise NotConfigured('missing botocore library')
    _l_(20931)
try:
    import botocore.session
    _l_(20934)

except ImportError:
    pass
session = botocore.session.get_session()
_l_(20935)
self.s3_client = session.create_client(
    's3',
    aws_access_key_id=self.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY,
    aws_session_token=self.AWS_SESSION_TOKEN,
    endpoint_url=self.AWS_ENDPOINT_URL,
    region_name=self.AWS_REGION_NAME,
    use_ssl=self.AWS_USE_SSL,
    verify=self.AWS_VERIFY
)
_l_(20936)
if not uri.startswith("s3://"):
    _l_(20938)

    raise ValueError(f"Incorrect URI scheme in {uri}, expected 's3'")
    _l_(20937)
self.bucket, self.prefix = uri[5:].split('/', 1)
_l_(20939)
