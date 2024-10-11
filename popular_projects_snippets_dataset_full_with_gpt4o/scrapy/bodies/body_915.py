# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
self._finished = finished
self._txresponse = txresponse
self._request = request
self._bodybuf = BytesIO()
self._maxsize = maxsize
self._warnsize = warnsize
self._fail_on_dataloss = fail_on_dataloss
self._fail_on_dataloss_warned = False
self._reached_warnsize = False
self._bytes_received = 0
self._certificate = None
self._ip_address = None
self._crawler = crawler
