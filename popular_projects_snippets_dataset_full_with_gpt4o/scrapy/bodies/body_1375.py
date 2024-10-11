# Extracted from ./data/repos/scrapy/scrapy/dupefilters.py
self.file = None
self.fingerprinter = fingerprinter or RequestFingerprinter()
self.fingerprints: Set[str] = set()
self.logdupes = True
self.debug = debug
self.logger = logging.getLogger(__name__)
if path:
    self.file = Path(path, 'requests.seen').open('a+', encoding="utf-8")
    self.file.seek(0)
    self.fingerprints.update(x.rstrip() for x in self.file)
