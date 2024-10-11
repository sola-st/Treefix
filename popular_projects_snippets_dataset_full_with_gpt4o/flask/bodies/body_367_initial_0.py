obj = type('MockObject', (object,), {})() # pragma: no cover
self = type('Mock', (object,), {'null_session_class': type('NullSession', (object,), {})})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
"""Checks if a given object is a null session.  Null sessions are
        not asked to be saved.

        This checks if the object is an instance of :attr:`null_session_class`
        by default.
        """
aux = isinstance(obj, self.null_session_class)
_l_(22946)
exit(aux)
