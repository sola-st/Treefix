# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
from google.cloud import storage
client = storage.Client(project=self.GCS_PROJECT_ID)
bucket, prefix = uri[5:].split('/', 1)
self.bucket = client.bucket(bucket)
self.prefix = prefix
permissions = self.bucket.test_iam_permissions(
    ['storage.objects.get', 'storage.objects.create']
)
if 'storage.objects.get' not in permissions:
    logger.warning(
        "No 'storage.objects.get' permission for GSC bucket %(bucket)s. "
        "Checking if files are up to date will be impossible. Files will be downloaded every time.",
        {'bucket': bucket}
    )
if 'storage.objects.create' not in permissions:
    logger.error(
        "No 'storage.objects.create' permission for GSC bucket %(bucket)s. Saving files will be impossible!",
        {'bucket': bucket}
    )
