from types import SimpleNamespace # pragma: no cover

self = SimpleNamespace() # pragma: no cover
self.conn = SimpleNamespace() # pragma: no cover
self.conn.local_settings = SimpleNamespace() # pragma: no cover
self.conn.local_settings.max_concurrent_streams = 5 # pragma: no cover
self.conn.remote_settings = SimpleNamespace() # pragma: no cover
self.conn.remote_settings.max_concurrent_streams = 10 # pragma: no cover

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
_l_(9337)
exit(aux)
