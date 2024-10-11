from unittest.mock import Mock # pragma: no cover
from twisted.internet.defer import Deferred # pragma: no cover

self = Mock() # pragma: no cover
reason = Mock() # pragma: no cover
connectionDone = Mock() # pragma: no cover
StreamCloseReason = type('StreamCloseReason', (object,), {'CONNECTION_LOST': 'connection_lost', 'INACTIVE': 'inactive'}) # pragma: no cover
self.setTimeout = Mock() # pragma: no cover
reason.check = Mock(return_value=False) # pragma: no cover
self._conn_lost_errors = [] # pragma: no cover
self._conn_lost_deferred = Mock() # pragma: no cover
self._conn_lost_deferred.callback = Mock() # pragma: no cover
self.streams = {1: Mock(metadata={'request_sent': True}), 2: Mock(metadata={'request_sent': False})} # pragma: no cover
self.streams[1].close = Mock() # pragma: no cover
self.streams[2].close = Mock() # pragma: no cover
self.metadata = {'active_streams': 2} # pragma: no cover
self._pending_request_stream_pool = [] # pragma: no cover
self.conn = Mock() # pragma: no cover
self.conn.close_connection = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
from l3.Runtime import _l_
"""Called by Twisted when the transport connection is lost.
        No need to write anything to transport here.
        """
# Cancel the timeout if not done yet
self.setTimeout(None)
_l_(18601)

# Notify the connection pool instance such that no new requests are
# sent over current connection
if not reason.check(connectionDone):
    _l_(18603)

    self._conn_lost_errors.append(reason)
    _l_(18602)

self._conn_lost_deferred.callback(self._conn_lost_errors)
_l_(18604)

for stream in self.streams.values():
    _l_(18609)

    if stream.metadata['request_sent']:
        _l_(18607)

        close_reason = StreamCloseReason.CONNECTION_LOST
        _l_(18605)
    else:
        close_reason = StreamCloseReason.INACTIVE
        _l_(18606)
    stream.close(close_reason, self._conn_lost_errors, from_protocol=True)
    _l_(18608)

self.metadata['active_streams'] -= len(self.streams)
_l_(18610)
self.streams.clear()
_l_(18611)
self._pending_request_stream_pool.clear()
_l_(18612)
self.conn.close_connection()
_l_(18613)
