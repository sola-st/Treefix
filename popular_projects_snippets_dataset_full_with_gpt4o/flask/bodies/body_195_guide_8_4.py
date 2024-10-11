class MockDeserializer:# pragma: no cover
    def deserialize(self, s, **kwargs):# pragma: no cover
        raise NotImplementedError('Custom error message') # pragma: no cover
mock_instance = MockDeserializer() # pragma: no cover
s = 'dummy text' # pragma: no cover
kwargs = {} # pragma: no cover
try:# pragma: no cover
    mock_instance.deserialize(s, **kwargs)# pragma: no cover
except NotImplementedError as e:# pragma: no cover
    print(e) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Deserialize data as JSON.

        :param s: Text or UTF-8 bytes.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22621)
