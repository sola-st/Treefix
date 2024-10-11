import logging # pragma: no cover
from enum import Enum # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
data = b'Test data' # pragma: no cover
flow_controlled_length = 25 # pragma: no cover
class StreamCloseReason(Enum): MAXSIZE_EXCEEDED = 1 # pragma: no cover
logger = logging.getLogger(__name__) # pragma: no cover
handler = logging.StreamHandler() # pragma: no cover
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # pragma: no cover
handler.setFormatter(formatter) # pragma: no cover
logger.addHandler(handler) # pragma: no cover
logger.setLevel(logging.WARNING) # pragma: no cover
self._response = {'body': type('Mock', (object,), {'write': lambda x: None})(), 'flow_controlled_size': 0} # pragma: no cover
self._download_maxsize = 100 # pragma: no cover
def reset_stream(reason): pass # pragma: no cover
self.reset_stream = reset_stream # pragma: no cover
self._log_warnsize = True # pragma: no cover
self.metadata = {} # pragma: no cover
self._download_warnsize = 50 # pragma: no cover
self._request = 'sample_request' # pragma: no cover
logger.warning = lambda msg: print(f'WARNING: {msg}') # pragma: no cover
self._protocol = type('Mock', (object,), {'conn': type('Mock', (object,), {'acknowledge_received_data': lambda x, y: None})()})() # pragma: no cover
self.stream_id = 1 # pragma: no cover

import logging # pragma: no cover
from enum import Enum # pragma: no cover
from io import BytesIO # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
data = b'Test data' # pragma: no cover
flow_controlled_length = len(data) # pragma: no cover
class StreamCloseReason(Enum): MAXSIZE_EXCEEDED = 1 # pragma: no cover
logger = logging.getLogger(__name__) # pragma: no cover
handler = logging.StreamHandler() # pragma: no cover
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # pragma: no cover
handler.setFormatter(formatter) # pragma: no cover
logger.addHandler(handler) # pragma: no cover
logger.setLevel(logging.WARNING) # pragma: no cover
self._response = {'body': BytesIO(), 'flow_controlled_size': 0} # pragma: no cover
self._download_maxsize = 100 # pragma: no cover
def reset_stream(reason): pass # pragma: no cover
self.reset_stream = reset_stream # pragma: no cover
self._log_warnsize = True # pragma: no cover
self.metadata = {} # pragma: no cover
self._download_warnsize = 50 # pragma: no cover
self._request = 'sample_request' # pragma: no cover
logger.warning = lambda msg: print(f'WARNING: {msg}') # pragma: no cover
self._protocol = type('Mock', (object,), {'conn': type('Mock', (object,), {'acknowledge_received_data': lambda size, stream_id: print(f'Acknowledged {size} bytes for stream {stream_id}')})()})() # pragma: no cover
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
