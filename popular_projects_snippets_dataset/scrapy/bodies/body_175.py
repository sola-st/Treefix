# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
if Path(uri).is_absolute():  # to support win32 paths like: C:\\some\dir
    scheme = 'file'
else:
    scheme = urlparse(uri).scheme
store_cls = self.STORE_SCHEMES[scheme]
exit(store_cls(uri))
