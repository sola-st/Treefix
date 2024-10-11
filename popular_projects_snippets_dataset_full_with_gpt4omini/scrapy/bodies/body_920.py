# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/s3.py
if not is_botocore_available():
    raise NotConfigured('missing botocore library')

if not aws_access_key_id:
    aws_access_key_id = settings['AWS_ACCESS_KEY_ID']
if not aws_secret_access_key:
    aws_secret_access_key = settings['AWS_SECRET_ACCESS_KEY']
if not aws_session_token:
    aws_session_token = settings['AWS_SESSION_TOKEN']

# If no credentials could be found anywhere,
# consider this an anonymous connection request by default;
# unless 'anon' was set explicitly (True/False).
anon = kw.get('anon')
if anon is None and not aws_access_key_id and not aws_secret_access_key:
    kw['anon'] = True
self.anon = kw.get('anon')

self._signer = None
import botocore.auth
import botocore.credentials
kw.pop('anon', None)
if kw:
    raise TypeError(f'Unexpected keyword arguments: {kw}')
if not self.anon:
    SignerCls = botocore.auth.AUTH_TYPE_MAPS['s3']
    self._signer = SignerCls(botocore.credentials.Credentials(
        aws_access_key_id, aws_secret_access_key, aws_session_token))

_http_handler = create_instance(
    objcls=httpdownloadhandler,
    settings=settings,
    crawler=crawler,
)
self._download_http = _http_handler.download_request
