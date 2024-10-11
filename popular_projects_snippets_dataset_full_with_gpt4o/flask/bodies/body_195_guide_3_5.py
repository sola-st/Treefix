import json # pragma: no cover

class MockDeserializer:# pragma: no cover
    def deserialize(self, s, **kwargs):# pragma: no cover
        if not s:# pragma: no cover
            raise ValueError('Input is empty')# pragma: no cover
        try:# pragma: no cover
            return json.loads(s, **kwargs)# pragma: no cover
        except json.JSONDecodeError as e:# pragma: no cover
            raise ValueError('Invalid JSON data') from e# pragma: no cover
# pragma: no cover
deserializer = MockDeserializer()# pragma: no cover
s = json.dumps({'key': 'value'})# pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Deserialize data as JSON.

        :param s: Text or UTF-8 bytes.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22621)
