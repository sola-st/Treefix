from typing import Dict, List, Any # pragma: no cover
class MockReason: # pragma: no cover
    def check(self, reason): # pragma: no cover
        return reason == connectionDone # pragma: no cover
class MockStreamCloseReason: # pragma: no cover
    CONNECTION_LOST = 'connection_lost' # pragma: no cover
    INACTIVE = 'inactive' # pragma: no cover

self = type('Mock', (object,), { # pragma: no cover
    'setTimeout': lambda self, val: None, # pragma: no cover
    '_conn_lost_errors': [], # pragma: no cover
    '_conn_lost_deferred': type('MockDeferred', (object,), { # pragma: no cover
        'callback': lambda self, errors: None # pragma: no cover
    })(), # pragma: no cover
    'streams': {0: {'metadata': {'request_sent': True}}, 1: {'metadata': {'request_sent': False}}}, # pragma: no cover
    'metadata': {'active_streams': 2}, # pragma: no cover
    '_pending_request_stream_pool': [], # pragma: no cover
    'conn': type('MockConnection', (object,), { # pragma: no cover
        'close_connection': lambda self: None # pragma: no cover
    })() # pragma: no cover
})() # pragma: no cover
reason = MockReason() # pragma: no cover
connectionDone = 'connection_done' # pragma: no cover
StreamCloseReason = MockStreamCloseReason # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
from l3.Runtime import _l_
"""Called by Twisted when the transport connection is lost.
        No need to write anything to transport here.
        """
# Cancel the timeout if not done yet
self.setTimeout(None)
_l_(7762)

# Notify the connection pool instance such that no new requests are
# sent over current connection
if not reason.check(connectionDone):
    _l_(7764)

    self._conn_lost_errors.append(reason)
    _l_(7763)

self._conn_lost_deferred.callback(self._conn_lost_errors)
_l_(7765)

for stream in self.streams.values():
    _l_(7770)

    if stream.metadata['request_sent']:
        _l_(7768)

        close_reason = StreamCloseReason.CONNECTION_LOST
        _l_(7766)
    else:
        close_reason = StreamCloseReason.INACTIVE
        _l_(7767)
    stream.close(close_reason, self._conn_lost_errors, from_protocol=True)
    _l_(7769)

self.metadata['active_streams'] -= len(self.streams)
_l_(7771)
self.streams.clear()
_l_(7772)
self._pending_request_stream_pool.clear()
_l_(7773)
self.conn.close_connection()
_l_(7774)
