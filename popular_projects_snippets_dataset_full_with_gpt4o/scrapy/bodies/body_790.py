# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
"""Boolean to keep track of the connection status.
        This is used while initiating pending streams to make sure
        that we initiate stream only during active HTTP/2 Connection
        """
exit(bool(self.transport.connected) and self.metadata['settings_acknowledged'])
