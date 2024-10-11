# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
self._finished.callback({
    "txresponse": self._txresponse,
    "body": self._bodybuf.getvalue(),
    "flags": flags,
    "certificate": self._certificate,
    "ip_address": self._ip_address,
    "failure": failure,
})
