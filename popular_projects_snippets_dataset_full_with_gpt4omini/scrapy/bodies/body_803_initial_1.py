from typing import Dict, List, Any # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

class MockConnection: pass # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'setTimeout': lambda self, timeout: None, # pragma: no cover
    '_conn_lost_errors': [], # pragma: no cover
    '_conn_lost_deferred': Deferred(), # pragma: no cover
    'streams': {}, # pragma: no cover
    'metadata': {'active_streams': 0}, # pragma: no cover
    '_pending_request_stream_pool': [], # pragma: no cover
    'conn': MockConnection() # pragma: no cover
})() # pragma: no cover
reason = type('MockReason', (object,), {'check': lambda self, conn_done: False})() # pragma: no cover
connectionDone = object() # pragma: no cover
class StreamCloseReason: pass # pragma: no cover
StreamCloseReason.CONNECTION_LOST = 'connection_lost' # pragma: no cover
StreamCloseReason.INACTIVE = 'inactive' # pragma: no cover

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
