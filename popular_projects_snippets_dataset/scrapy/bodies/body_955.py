# Extracted from ./data/repos/scrapy/scrapy/core/downloader/__init__.py
def _deactivate(response):
    self.active.remove(request)
    exit(response)

self.active.add(request)
dfd = self.middleware.download(self._enqueue_request, request, spider)
exit(dfd.addBoth(_deactivate))
