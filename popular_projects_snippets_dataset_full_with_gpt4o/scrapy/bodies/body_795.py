# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
from l3.Runtime import _l_
""" Write data to the underlying transport connection
        from the HTTP2 connection instance if any
        """
# Reset the idle timeout as connection is still actively sending data
self.resetTimeout()
_l_(18573)

data = self.conn.data_to_send()
_l_(18574)
self.transport.write(data)
_l_(18575)
