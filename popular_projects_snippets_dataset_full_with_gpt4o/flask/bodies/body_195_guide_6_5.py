import json # pragma: no cover

class MockDeserializer:# pragma: no cover
    def __init__(self, s, **kwargs):# pragma: no cover
        self.s = s# pragma: no cover
        self.kwargs = kwargs# pragma: no cover
    def deserialize(self):# pragma: no cover
        print('Deserializing...')# pragma: no cover
# pragma: no cover
s = '{"key": "value"}'# pragma: no cover
kwargs = {}# pragma: no cover
# pragma: no cover
deserializer = MockDeserializer(s, **kwargs)# pragma: no cover
deserializer.deserialize() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Deserialize data as JSON.

        :param s: Text or UTF-8 bytes.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22621)
