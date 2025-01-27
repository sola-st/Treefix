# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
if not is_botocore_available():
    raise NotConfigured('missing botocore library')
u = urlparse(uri)
self.bucketname = u.hostname
self.access_key = u.username or access_key
self.secret_key = u.password or secret_key
self.session_token = session_token
self.keyname = u.path[1:]  # remove first "/"
self.acl = acl
self.endpoint_url = endpoint_url
import botocore.session
session = botocore.session.get_session()
self.s3_client = session.create_client(
    's3', aws_access_key_id=self.access_key,
    aws_secret_access_key=self.secret_key,
    aws_session_token=self.session_token,
    endpoint_url=self.endpoint_url)
if feed_options and feed_options.get('overwrite', True) is False:
    logger.warning('S3 does not support appending to files. To '
                   'suppress this warning, remove the overwrite '
                   'option from your FEEDS setting or set it to True.')
