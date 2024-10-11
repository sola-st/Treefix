self = type('Mock', (object,), {'metadata': {'request_sent': False}, 'reset_stream': lambda self, reason: print(f'Resetting stream due to {reason}'), 'close': lambda self, reason: print(f'Closing stream due to {reason}')})() # pragma: no cover
StreamCloseReason = type('StreamCloseReason', (object,), {'CANCELLED': 'CANCELLED'}) # pragma: no cover

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
