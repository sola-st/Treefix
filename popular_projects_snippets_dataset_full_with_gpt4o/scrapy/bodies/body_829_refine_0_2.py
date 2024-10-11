from io import StringIO # pragma: no cover
import logging # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
self._response = {'body': StringIO(), 'flow_controlled_size': 0} # pragma: no cover
self._download_maxsize = 1024 * 1024 * 10 # 10 MB # pragma: no cover
self.reset_stream = lambda reason: None # pragma: no cover
StreamCloseReason = type('MockStreamCloseReason', (object,), {'MAXSIZE_EXCEEDED': 'maxsize_exceeded'}) # pragma: no cover
self._log_warnsize = True # pragma: no cover
self.metadata = {} # pragma: no cover
self._download_warnsize = 1024 * 1024 * 5 # 5 MB # pragma: no cover
self._request = 'http://example.com' # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover
logger.warning = lambda msg: print(f'WARNING: {msg}') # pragma: no cover
self._protocol = type('MockProtocol', (object,), {})() # pragma: no cover
self._protocol.conn = type('MockConn', (object,), {'acknowledge_received_data': lambda size, stream_id: None})() # pragma: no cover
self.stream_id = 1 # pragma: no cover
data = 'sample data' # pragma: no cover
flow_controlled_length = len(data) # pragma: no cover

from io import StringIO # pragma: no cover
import logging # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
self._response = {'body': StringIO(), 'flow_controlled_size': 0} # pragma: no cover
self._download_maxsize = 1024 * 1024 * 10 # 10 MB # pragma: no cover
self.reset_stream = lambda reason: None # pragma: no cover
StreamCloseReason = type('MockStreamCloseReason', (object,), {'MAXSIZE_EXCEEDED': 'maxsize_exceeded'}) # pragma: no cover
self._log_warnsize = True # pragma: no cover
self.metadata = {} # pragma: no cover
self._download_warnsize = 1024 * 1024 * 5 # 5 MB # pragma: no cover
self._request = 'http://example.com' # pragma: no cover
logger = logging.getLogger('example_logger') # pragma: no cover
logger.warning = lambda msg: print(f'WARNING: {msg}') # pragma: no cover
self._protocol = type('MockProtocol', (object,), {})() # pragma: no cover
self._protocol.conn = type('MockConn', (object,), {'acknowledge_received_data': lambda size, stream_id: None})() # pragma: no cover
self.stream_id = 1 # pragma: no cover
data = 'sample data' # pragma: no cover
flow_controlled_length = len(data) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
from l3.Runtime import _l_
self._response['body'].write(data)
_l_(21209)
self._response['flow_controlled_size'] += flow_controlled_length
_l_(21210)

# We check maxsize here in case the Content-Length header was not received
if self._download_maxsize and self._response['flow_controlled_size'] > self._download_maxsize:
    _l_(21213)

    self.reset_stream(StreamCloseReason.MAXSIZE_EXCEEDED)
    _l_(21211)
    exit()
    _l_(21212)

if self._log_warnsize:
    _l_(21217)

    self.metadata['reached_warnsize'] = True
    _l_(21214)
    warning_msg = (
        f'Received more ({self._response["flow_controlled_size"]}) bytes than download '
        f'warn size ({self._download_warnsize}) in request {self._request}'
    )
    _l_(21215)
    logger.warning(warning_msg)
    _l_(21216)

# Acknowledge the data received
self._protocol.conn.acknowledge_received_data(
    self._response['flow_controlled_size'],
    self.stream_id
)
_l_(21218)
