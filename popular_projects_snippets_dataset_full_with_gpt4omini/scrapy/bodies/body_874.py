# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/__init__.py
scheme = urlparse_cached(request).scheme
handler = self._get_handler(scheme)
if not handler:
    raise NotSupported(f"Unsupported URL scheme '{scheme}': {self._notconfigured[scheme]}")
exit(handler.download_request(request, spider))
