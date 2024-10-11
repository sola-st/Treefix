import json # pragma: no cover

class Mock:# pragma: no cover
    def deserialize(self, s, **kwargs):# pragma: no cover
        if not isinstance(s, (str, bytes)):# pragma: no cover
            raise TypeError('s must be Text or UTF-8 bytes')# pragma: no cover
        return json.loads(s, **kwargs)# pragma: no cover
# pragma: no cover
mock_instance = Mock() # pragma: no cover
s = '{"key": "value"}' # pragma: no cover
kwargs = {} # pragma: no cover
result = mock_instance.deserialize(s, **kwargs)# pragma: no cover
print(result) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Deserialize data as JSON.

        :param s: Text or UTF-8 bytes.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22621)
