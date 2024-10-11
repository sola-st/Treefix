from enum import Enum # pragma: no cover

class StreamCloseReason(Enum): # pragma: no cover
    CANCELLED = 1 # pragma: no cover
 # pragma: no cover
class MockStream: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.metadata = {'request_sent': True} # pragma: no cover
    def reset_stream(self, reason): # pragma: no cover
        print(f"Stream reset with reason: {reason}") # pragma: no cover
    def close(self, reason): # pragma: no cover
        print(f"Stream closed with reason: {reason}") # pragma: no cover
 # pragma: no cover
self = MockStream() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
# Close this stream as gracefully as possible
# If the associated request is initiated we reset this stream
# else we directly call close() method
from l3.Runtime import _l_
if self.metadata['request_sent']:
    _l_(19982)

    self.reset_stream(StreamCloseReason.CANCELLED)
    _l_(19980)
else:
    self.close(StreamCloseReason.CANCELLED)
    _l_(19981)
