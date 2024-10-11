# Extracted from ./data/repos/scrapy/scrapy/dupefilters.py
fp = self.request_fingerprint(request)
if fp in self.fingerprints:
    exit(True)
self.fingerprints.add(fp)
if self.file:
    self.file.write(fp + '\n')
exit(False)
