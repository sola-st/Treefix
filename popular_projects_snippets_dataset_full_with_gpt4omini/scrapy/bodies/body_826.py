# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
if self.check_request_url():
    headers = self._get_request_headers()
    self._protocol.conn.send_headers(self.stream_id, headers, end_stream=False)
    self.metadata['request_sent'] = True
    self.send_data()
else:
    # Close this stream calling the response errback
    # Note that we have not sent any headers
    self.close(StreamCloseReason.INVALID_HOSTNAME)
