import logging # pragma: no cover
from enum import Enum # pragma: no cover
from io import BytesIO # pragma: no cover

data = b'some data' # pragma: no cover
flow_controlled_length = len(data) # pragma: no cover

import logging # pragma: no cover
from enum import Enum # pragma: no cover
from io import BytesIO # pragma: no cover

class StreamCloseReason(Enum): MAXSIZE_EXCEEDED = 1 # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._response = {'body': BytesIO(), 'flow_controlled_size': 0} # pragma: no cover
self._download_maxsize = 1000 # pragma: no cover
self._log_warnsize = True # pragma: no cover
self.metadata = {} # pragma: no cover
self._download_warnsize = 500 # pragma: no cover
self._request = 'some_request_data' # pragma: no cover
self._protocol = type('MockProtocol', (object,), {'conn': type('MockConnection', (object,), {'acknowledge_received_data': lambda size, stream_id: None})()})() # pragma: no cover
self.stream_id = 1 # pragma: no cover
data = b'Sample data' # pragma: no cover
flow_controlled_length = len(data) # pragma: no cover
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
