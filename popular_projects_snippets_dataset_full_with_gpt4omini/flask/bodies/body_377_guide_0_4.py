from typing import Callable # pragma: no cover

class MockRequestContext(object): # pragma: no cover
    def is_null_session(self): # pragma: no cover
        return False # pragma: no cover
    def handle_request(self): # pragma: no cover
        # Call the logic that includes the uncovered code # pragma: no cover
        if not self.is_null_session(): # pragma: no cover
            pass
 # pragma: no cover
request_context = MockRequestContext() # pragma: no cover
request_context.handle_request() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
"""This is called at the end of each request, after generating
        a response, before removing the request context. It is skipped
        if :meth:`is_null_session` returns ``True``.
        """
raise NotImplementedError()
_l_(8818)
