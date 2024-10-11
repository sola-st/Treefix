from unittest.mock import Mock, ANY # pragma: no cover
import logging # pragma: no cover

self = Mock() # pragma: no cover
self._response = {'body': Mock(write=Mock()), 'flow_controlled_size': 0} # pragma: no cover
data = b'some data to write' # pragma: no cover
flow_controlled_length = len(data) # pragma: no cover
StreamCloseReason = type('StreamCloseReason', (object,), {'MAXSIZE_EXCEEDED': 'maxsize_exceeded'}) # pragma: no cover
logger = logging.getLogger('test') # pragma: no cover
self._download_maxsize = 1000 # pragma: no cover
self.reset_stream = Mock() # pragma: no cover
self._log_warnsize = True # pragma: no cover
self.metadata = {'reached_warnsize': False} # pragma: no cover
self._download_warnsize = 500 # pragma: no cover
self._request = 'GET /some/resource' # pragma: no cover
logger.warning = Mock() # pragma: no cover
self._protocol = Mock() # pragma: no cover
self._protocol.conn = Mock() # pragma: no cover
self._protocol.conn.acknowledge_received_data = Mock() # pragma: no cover
self.stream_id = 1 # pragma: no cover

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
