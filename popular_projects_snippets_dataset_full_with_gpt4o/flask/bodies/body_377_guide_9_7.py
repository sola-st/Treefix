class MockRequestContext(object): # pragma: no cover
    def is_null_session(self): # pragma: no cover
        return False  # Ensure it returns False to execute NotImplementedError # pragma: no cover
 # pragma: no cover
request_context = MockRequestContext() # pragma: no cover
 # pragma: no cover
if not request_context.is_null_session(): # pragma: no cover
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
