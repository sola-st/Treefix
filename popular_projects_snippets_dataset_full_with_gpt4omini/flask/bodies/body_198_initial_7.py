from flask import Flask, Response, jsonify # pragma: no cover
import json # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = type('Mock', (object,), {'_prepare_response_obj': lambda self, args, kwargs: args[0] if args else kwargs, '_app': app, 'dumps': json.dumps})() # pragma: no cover
args = ('example_value',) # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Serialize the given arguments as JSON, and return a
        :class:`~flask.Response` object with the ``application/json``
        mimetype.

        The :func:`~flask.json.jsonify` function calls this method for
        the current application.

        Either positional or keyword arguments can be given, not both.
        If no arguments are given, ``None`` is serialized.

        :param args: A single value to serialize, or multiple values to
            treat as a list to serialize.
        :param kwargs: Treat as a dict to serialize.
        """
obj = self._prepare_response_obj(args, kwargs)
_l_(8803)
aux = self._app.response_class(self.dumps(obj), mimetype="application/json")
_l_(8804)
exit(aux)
