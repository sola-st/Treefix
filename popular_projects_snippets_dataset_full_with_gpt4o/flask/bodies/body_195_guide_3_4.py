class MockDeserializer:# pragma: no cover
    def deserialize(self, s, **kwargs):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
mock_deserializer = MockDeserializer()# pragma: no cover
# pragma: no cover
try:# pragma: no cover
    raise NotImplementedError()# pragma: no cover
except NotImplementedError:# pragma: no cover
    mock_deserializer.deserialize('{}') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Deserialize data as JSON.

        :param s: Text or UTF-8 bytes.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22621)
