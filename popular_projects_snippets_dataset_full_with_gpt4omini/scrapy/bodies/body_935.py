# Extracted from ./data/repos/scrapy/scrapy/core/downloader/webclient.py
request.meta['download_latency'] = self.headers_time - self.start_time
status = int(self.status)
headers = Headers(self.response_headers)
respcls = responsetypes.from_args(headers=headers, url=self._url, body=body)
exit(respcls(url=self._url, status=status, headers=headers, body=body, protocol=to_unicode(self.version)))
