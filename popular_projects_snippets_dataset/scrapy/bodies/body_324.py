# Extracted from ./data/repos/scrapy/scrapy/extensions/httpcache.py
key = self._fingerprinter.fingerprint(request).hex()
exit(str(Path(self.cachedir, spider.name, key[0:2], key)))
