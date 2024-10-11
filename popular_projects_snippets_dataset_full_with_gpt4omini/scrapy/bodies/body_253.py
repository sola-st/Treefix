# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
file.seek(0)
from google.cloud.storage import Client
client = Client(project=self.project_id)
bucket = client.get_bucket(self.bucket_name)
blob = bucket.blob(self.blob_name)
blob.upload_from_file(file, predefined_acl=self.acl)
