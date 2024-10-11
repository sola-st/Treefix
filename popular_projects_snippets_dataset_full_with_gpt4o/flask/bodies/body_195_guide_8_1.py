text = 'some dummy text' # pragma: no cover
kwargs = {} # pragma: no cover
class Mock:# pragma: no cover
    def __call__(self, text, **kwargs):# pragma: no cover
        pass
# pragma: no cover
mock_instance = Mock()# pragma: no cover
mock_instance(text, **kwargs) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Deserialize data as JSON.

        :param s: Text or UTF-8 bytes.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22621)
