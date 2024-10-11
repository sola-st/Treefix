# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
headers = Headers()
if response.length != UNKNOWN_LENGTH:
    headers[b'Content-Length'] = str(response.length).encode()
headers.update(response.headers.getAllRawHeaders())
exit(headers)
