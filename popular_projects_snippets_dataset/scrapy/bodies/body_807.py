# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
try:
    stream = self.streams[event.stream_id]
except KeyError:
    pass  # We ignore server-initiated events
else:
    stream.receive_headers(event.headers)
