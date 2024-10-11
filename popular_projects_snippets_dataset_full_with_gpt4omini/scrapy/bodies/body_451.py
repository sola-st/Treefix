# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
"""Creates autospec mocks for google-cloud-storage Client, Bucket and Blob
    classes and set their proper return values.
    """
from google.cloud.storage import Client, Bucket, Blob
client_mock = mock.create_autospec(Client)

bucket_mock = mock.create_autospec(Bucket)
client_mock.get_bucket.return_value = bucket_mock

blob_mock = mock.create_autospec(Blob)
bucket_mock.blob.return_value = blob_mock

exit((client_mock, bucket_mock, blob_mock))
