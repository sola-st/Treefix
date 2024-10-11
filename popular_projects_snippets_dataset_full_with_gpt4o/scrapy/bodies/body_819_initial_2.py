self = type('Mock', (object,), {# pragma: no cover
    'metadata': {'request_sent': True},# pragma: no cover
    'reset_stream': lambda self, reason: print(f'reset_stream called with {reason}'),# pragma: no cover
    'close': lambda self, reason: print(f'close called with {reason}')# pragma: no cover
})() # pragma: no cover
StreamCloseReason = type('StreamCloseReason', (object,), {'CANCELLED': 'cancelled'}) # pragma: no cover

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
