import botocore # pragma: no cover

def is_botocore_available(): return True # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.AWS_ACCESS_KEY_ID = 'mock_access_key' # pragma: no cover
self.AWS_SECRET_ACCESS_KEY = 'mock_secret_key' # pragma: no cover
self.AWS_SESSION_TOKEN = 'mock_session_token' # pragma: no cover
self.AWS_ENDPOINT_URL = 'https://mock-endpoint.com' # pragma: no cover
self.AWS_REGION_NAME = 'us-east-1' # pragma: no cover
self.AWS_USE_SSL = True # pragma: no cover
self.AWS_VERIFY = True # pragma: no cover
uri = 's3://my_bucket/my_prefix' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
from l3.Runtime import _l_
if not is_botocore_available():
    _l_(9572)

    raise NotConfigured('missing botocore library')
    _l_(9571)
try:
    import botocore.session
    _l_(9574)

except ImportError:
    pass
session = botocore.session.get_session()
_l_(9575)
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
_l_(9576)
if not uri.startswith("s3://"):
    _l_(9578)

    raise ValueError(f"Incorrect URI scheme in {uri}, expected 's3'")
    _l_(9577)
self.bucket, self.prefix = uri[5:].split('/', 1)
_l_(9579)
