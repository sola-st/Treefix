# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
for name, value in headers:
    self._response['headers'].appendlist(name, value)

# Check if we exceed the allowed max data size which can be received
expected_size = int(self._response['headers'].get(b'Content-Length', -1))
if self._download_maxsize and expected_size > self._download_maxsize:
    self.reset_stream(StreamCloseReason.MAXSIZE_EXCEEDED)
    exit()

if self._log_warnsize:
    self.metadata['reached_warnsize'] = True
    warning_msg = (
        f'Expected response size ({expected_size}) larger than '
        f'download warn size ({self._download_warnsize}) in request {self._request}'
    )
    logger.warning(warning_msg)
