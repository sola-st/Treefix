# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
"""Called by Twisted when the connection is established. We can start
        sending some data now: we should open with the connection preamble.
        """
# Initialize the timeout
self.setTimeout(self.IDLE_TIMEOUT)

destination = self.transport.getPeer()
self.metadata['ip_address'] = ipaddress.ip_address(destination.host)

# Initiate H2 Connection
self.conn.initiate_connection()
self._write_to_transport()
