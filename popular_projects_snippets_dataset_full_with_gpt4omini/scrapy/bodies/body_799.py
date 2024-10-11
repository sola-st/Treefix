# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
"""
        Close the connection if it's not made via the expected protocol
        """
if self.transport.negotiatedProtocol is not None and self.transport.negotiatedProtocol != PROTOCOL_NAME:
    # we have not initiated the connection yet, no need to send a GOAWAY frame to the remote peer
    self._lose_connection_with_error([InvalidNegotiatedProtocol(self.transport.negotiatedProtocol)])
