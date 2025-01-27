# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
self.project_id = project_id
self.acl = acl
u = urlparse(uri)
self.bucket_name = u.hostname
self.blob_name = u.path[1:]  # remove first "/"
