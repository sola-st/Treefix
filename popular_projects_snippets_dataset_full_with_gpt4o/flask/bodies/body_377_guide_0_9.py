from types import MethodType # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.is_null_session = MethodType(lambda self: False, self) # pragma: no cover
 # pragma: no cover
mock_instance = Mock() # pragma: no cover
 # pragma: no cover
# Below conditions are based on context and purpose descriptions from the code snippet. # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
"""This is called at the end of each request, after generating
        a response, before removing the request context. It is skipped
        if :meth:`is_null_session` returns ``True``.
        """
raise NotImplementedError()
_l_(22928)
