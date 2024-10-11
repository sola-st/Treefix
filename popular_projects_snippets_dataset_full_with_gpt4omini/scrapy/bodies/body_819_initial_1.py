from enum import Enum # pragma: no cover

class StreamCloseReason(Enum): CANCELLED = 'cancelled' # pragma: no cover
class Mock: pass # pragma: no cover
self = type('MockStream', (Mock,), {'metadata': {'request_sent': False}, 'reset_stream': lambda self, reason: print(f'Stream reset with reason: {reason}'), 'close': lambda self, reason: print(f'Stream closed with reason: {reason}'),})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
# Close this stream as gracefully as possible
# If the associated request is initiated we reset this stream
# else we directly call close() method
from l3.Runtime import _l_
if self.metadata['request_sent']:
    _l_(8889)

    self.reset_stream(StreamCloseReason.CANCELLED)
    _l_(8887)
else:
    self.close(StreamCloseReason.CANCELLED)
    _l_(8888)
