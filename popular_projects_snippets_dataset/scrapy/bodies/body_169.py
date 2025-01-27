# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
if not uri.startswith("ftp://"):
    raise ValueError(f"Incorrect URI scheme in {uri}, expected 'ftp'")
u = urlparse(uri)
self.port = u.port
self.host = u.hostname
self.port = int(u.port or 21)
self.username = u.username or self.FTP_USERNAME
self.password = u.password or self.FTP_PASSWORD
self.basedir = u.path.rstrip('/')
