from flask import Flask, g, session # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = app # pragma: no cover
self.before_request_funcs = {None: []} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Register a function to run before each request.

        For example, this can be used to open a database connection, or
        to load the logged in user from the session.

        .. code-block:: python

            @app.before_request
            def load_user():
                if "user_id" in session:
                    g.user = db.session.get(session["user_id"])

        The function will be called without any arguments. If it returns
        a non-``None`` value, the value is handled as if it was the
        return value from the view, and further request handling is
        stopped.
        """
self.before_request_funcs.setdefault(None, []).append(f)
_l_(5355)
aux = f
_l_(5356)
exit(aux)
