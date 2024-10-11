from types import MethodType # pragma: no cover

class MockSession: # pragma: no cover
    def is_null_session(self): # pragma: no cover
        return False  # Returning False to ensure the NotImplementedError is raised # pragma: no cover
 # pragma: no cover
mock_session = MockSession() # pragma: no cover
mock_session.is_null_session = MethodType(mock_session.is_null_session, mock_session) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
"""This is called at the end of each request, after generating
        a response, before removing the request context. It is skipped
        if :meth:`is_null_session` returns ``True``.
        """
raise NotImplementedError()
_l_(22928)
