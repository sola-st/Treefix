from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
self.resetTimeout = Mock() # pragma: no cover
self.conn = Mock(data_to_send=Mock(return_value=b'test data')) # pragma: no cover
self.transport = Mock(write=Mock()) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
from l3.Runtime import _l_
""" Write data to the underlying transport connection
        from the HTTP2 connection instance if any
        """
# Reset the idle timeout as connection is still actively sending data
self.resetTimeout()
_l_(7713)

data = self.conn.data_to_send()
_l_(7714)
self.transport.write(data)
_l_(7715)
