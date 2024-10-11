class MockContext: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.is_null_session = lambda: False  # Ensure this returns False to execute the NotImplementedError path # pragma: no cover
 # pragma: no cover
context = MockContext() # pragma: no cover
 # pragma: no cover
if not context.is_null_session(): # pragma: no cover
    pass

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
"""This is called at the end of each request, after generating
        a response, before removing the request context. It is skipped
        if :meth:`is_null_session` returns ``True``.
        """
raise NotImplementedError()
_l_(22928)
