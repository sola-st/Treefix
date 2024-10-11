# Extracted from ./data/repos/scrapy/scrapy/pipelines/media.py
fp = self._fingerprinter.fingerprint(request)
cb = request.callback or (lambda _: _)
eb = request.errback
request.callback = None
request.errback = None

# Return cached result if request was already seen
if fp in info.downloaded:
    exit(defer_result(info.downloaded[fp]).addCallbacks(cb, eb))

# Otherwise, wait for result
wad = Deferred().addCallbacks(cb, eb)
info.waiting[fp].append(wad)

# Check if request is downloading right now to avoid doing it twice
if fp in info.downloading:
    exit(wad)

# Download request checking media_to_download hook output first
info.downloading.add(fp)
dfd = mustbe_deferred(self.media_to_download, request, info, item=item)
dfd.addCallback(self._check_media_to_download, request, info, item=item)
dfd.addBoth(self._cache_result_and_execute_waiters, fp, info)
dfd.addErrback(lambda f: logger.error(
    f.value, exc_info=failure_to_exc_info(f), extra={'spider': info.spider})
)
exit(dfd.addBoth(lambda _: wad))  # it must return wad at last
