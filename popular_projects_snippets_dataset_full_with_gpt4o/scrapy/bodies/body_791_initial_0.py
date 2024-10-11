from typing import NamedTuple # pragma: no cover

class Settings(NamedTuple): # pragma: no cover
    max_concurrent_streams: int = 100 # pragma: no cover
 # pragma: no cover
class MockConn(NamedTuple): # pragma: no cover
    local_settings: Settings = Settings() # pragma: no cover
    remote_settings: Settings = Settings() # pragma: no cover
 # pragma: no cover
class MockSelf(NamedTuple): # pragma: no cover
    conn: MockConn = MockConn() # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/core/http2/protocol.py
from l3.Runtime import _l_
"""We keep total two streams for client (sending data) and
        server side (receiving data) for a single request. To be safe
        we choose the minimum. Since this value can change in event
        RemoteSettingsChanged we make variable a property.
        """
aux = min(
    self.conn.local_settings.max_concurrent_streams,
    self.conn.remote_settings.max_concurrent_streams
)
_l_(20421)
exit(aux)
