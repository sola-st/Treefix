from enum import Enum # pragma: no cover

class StreamCloseReason(Enum): CANCELLED = 1 # pragma: no cover
self = type('MockObject', (object,), {'metadata': {'request_sent': False}, 'reset_stream': lambda reason: None, 'close': lambda reason: None})() # pragma: no cover

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
