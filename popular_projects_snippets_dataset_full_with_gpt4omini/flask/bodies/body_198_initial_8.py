from flask import Flask, Response, jsonify # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = type('Mock', (object,), {'_app': app, '_prepare_response_obj': lambda self, args, kwargs: {'args': args, 'kwargs': kwargs}})() # pragma: no cover
args = ('value1', 'value2') # pragma: no cover
kwargs = {'key1': 'value3', 'key2': 'value4'} # pragma: no cover
self.dumps = lambda obj: jsonify(obj).get_data(as_text=True) # pragma: no cover

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
