from flask import Flask, request, g # pragma: no cover

app = Flask(__name__) # pragma: no cover
g = type('MockG', (object,), {'is_null_session': lambda: False})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/sessions.py
from l3.Runtime import _l_
"""This is called at the end of each request, after generating
        a response, before removing the request context. It is skipped
        if :meth:`is_null_session` returns ``True``.
        """
raise NotImplementedError()
_l_(8818)
