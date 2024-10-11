from io import BytesIO # pragma: no cover
import logging # pragma: no cover

self = type('Mock', (object,), { '_response': { 'body': BytesIO(), 'flow_controlled_size': 0 }, '_download_maxsize': 1024, '_log_warnsize': True, 'metadata': {}, '_download_warnsize': 800, '_request': 'GET /example', '_protocol': type('MockProtocol', (object,), { 'conn': type('MockConn', (object,), { 'acknowledge_received_data': lambda self, size, stream_id: None })() })() })() # pragma: no cover
data = b'example data' # pragma: no cover
flow_controlled_length = len(data) # pragma: no cover
StreamCloseReason = type('StreamCloseReason', (object,), { 'MAXSIZE_EXCEEDED': 'maxsize_exceeded' }) # pragma: no cover
logger = logging.getLogger('mock_logger') # pragma: no cover

from io import BytesIO # pragma: no cover
import logging # pragma: no cover

self = type('Mock', (object,), { '_response': { 'body': BytesIO(), 'flow_controlled_size': 0 }, '_download_maxsize': 1024, '_log_warnsize': True, 'metadata': {}, '_download_warnsize': 800, '_request': 'GET /example', 'stream_id': 1, '_protocol': type('MockProtocol', (object,), { 'conn': type('MockConn', (object,), { 'acknowledge_received_data': lambda self, size, stream_id: None })() })() })() # pragma: no cover
data = b'example data' # pragma: no cover
flow_controlled_length = len(data) # pragma: no cover
class StreamCloseReason:# pragma: no cover
    MAXSIZE_EXCEEDED = 'maxsize_exceeded' # pragma: no cover
logger = logging.getLogger('mock_logger') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/stream.py
from l3.Runtime import _l_
self._response['body'].write(data)
_l_(10072)
self._response['flow_controlled_size'] += flow_controlled_length
_l_(10073)

# We check maxsize here in case the Content-Length header was not received
if self._download_maxsize and self._response['flow_controlled_size'] > self._download_maxsize:
    _l_(10076)

    self.reset_stream(StreamCloseReason.MAXSIZE_EXCEEDED)
    _l_(10074)
    exit()
    _l_(10075)

if self._log_warnsize:
    _l_(10080)

    self.metadata['reached_warnsize'] = True
    _l_(10077)
    warning_msg = (
        f'Received more ({self._response["flow_controlled_size"]}) bytes than download '
        f'warn size ({self._download_warnsize}) in request {self._request}'
    )
    _l_(10078)
    logger.warning(warning_msg)
    _l_(10079)

# Acknowledge the data received
self._protocol.conn.acknowledge_received_data(
    self._response['flow_controlled_size'],
    self.stream_id
)
_l_(10081)
