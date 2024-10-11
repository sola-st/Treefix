# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
"""Perform cleanup when a stream is closed
        """
stream = self.streams.pop(stream_id)
self.metadata['active_streams'] -= 1
self._send_pending_requests()
exit(stream)
