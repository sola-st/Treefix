# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
"""Called when the connection times out.
        We lose the connection with TimeoutError"""

# Check whether there are open streams. If there are, we're going to
# want to use the error code PROTOCOL_ERROR. If there aren't, use
# NO_ERROR.
if (
    self.conn.open_outbound_streams > 0
    or self.conn.open_inbound_streams > 0
    or self.metadata['active_streams'] > 0
):
    error_code = ErrorCodes.PROTOCOL_ERROR
else:
    error_code = ErrorCodes.NO_ERROR
self.conn.close_connection(error_code=error_code)
self._write_to_transport()

self._lose_connection_with_error([
    TimeoutError(f"Connection was IDLE for more than {self.IDLE_TIMEOUT}s")
])
