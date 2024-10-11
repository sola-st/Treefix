# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
file.seek(0)
kwargs = {'ACL': self.acl} if self.acl else {}
self.s3_client.put_object(
    Bucket=self.bucketname, Key=self.keyname, Body=file,
    **kwargs)
file.close()
