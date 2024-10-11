errors = 1 # pragma: no cover
self = type('Mock', (object,), {'_conn_lost_errors': 0, 'transport': type('MockTransport', (object,), {'loseConnection': lambda self: None})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
from l3.Runtime import _l_
"""Helper function to lose the connection with the error sent as a
        reason"""
self._conn_lost_errors += errors
_l_(16472)
self.transport.loseConnection()
_l_(16473)
