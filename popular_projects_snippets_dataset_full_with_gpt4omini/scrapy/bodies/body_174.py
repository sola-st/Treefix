# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
s3store = cls.STORE_SCHEMES['s3']
s3store.AWS_ACCESS_KEY_ID = settings['AWS_ACCESS_KEY_ID']
s3store.AWS_SECRET_ACCESS_KEY = settings['AWS_SECRET_ACCESS_KEY']
s3store.AWS_SESSION_TOKEN = settings['AWS_SESSION_TOKEN']
s3store.AWS_ENDPOINT_URL = settings['AWS_ENDPOINT_URL']
s3store.AWS_REGION_NAME = settings['AWS_REGION_NAME']
s3store.AWS_USE_SSL = settings['AWS_USE_SSL']
s3store.AWS_VERIFY = settings['AWS_VERIFY']
s3store.POLICY = settings['FILES_STORE_S3_ACL']

gcs_store = cls.STORE_SCHEMES['gs']
gcs_store.GCS_PROJECT_ID = settings['GCS_PROJECT_ID']
gcs_store.POLICY = settings['FILES_STORE_GCS_ACL'] or None

ftp_store = cls.STORE_SCHEMES['ftp']
ftp_store.FTP_USERNAME = settings['FTP_USER']
ftp_store.FTP_PASSWORD = settings['FTP_PASSWORD']
ftp_store.USE_ACTIVE_MODE = settings.getbool('FEED_STORAGE_FTP_ACTIVE')

store_uri = settings['FILES_STORE']
exit(cls(store_uri, settings=settings))
