from enum import Enum # pragma: no cover

class MockStreamCloseReason(Enum): # pragma: no cover
    CANCELLED = 'cancelled' # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.metadata = {'request_sent': False} # pragma: no cover
    def reset_stream(self, reason): # pragma: no cover
        print(f'Stream reset due to: {reason}') # pragma: no cover
    def close(self, reason): # pragma: no cover
        print(f'Stream closed due to: {reason}') # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
StreamCloseReason = MockStreamCloseReason # pragma: no cover

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
