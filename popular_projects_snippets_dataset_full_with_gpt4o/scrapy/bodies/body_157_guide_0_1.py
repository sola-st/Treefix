import botocore.session # pragma: no cover
from botocore.exceptions import NoCredentialsError # pragma: no cover

uri = 's3://bucket_name/prefix' # pragma: no cover
def is_botocore_available(): return True # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover

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
