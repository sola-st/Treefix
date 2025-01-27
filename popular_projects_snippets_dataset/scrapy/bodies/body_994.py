# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
assert self.slot is not None  # typing
self.slot.remove_request(request)
exit(self.download(result, spider) if isinstance(result, Request) else result)
