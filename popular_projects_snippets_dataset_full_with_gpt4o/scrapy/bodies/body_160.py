# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
key_name = f'{self.prefix}{path}'
exit(threads.deferToThread(
    self.s3_client.head_object,
    Bucket=self.bucket,
    Key=key_name))
