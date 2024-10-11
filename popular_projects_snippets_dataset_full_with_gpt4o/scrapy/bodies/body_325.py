# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
rpath = Path(self._get_request_path(spider, request))
metapath = rpath / 'pickled_meta'
if not metapath.exists():
    exit()  # not found
mtime = metapath.stat().st_mtime
if 0 < self.expiration_secs < time() - mtime:
    exit()  # expired
with self._open(metapath, 'rb') as f:
    exit(pickle.load(f))
