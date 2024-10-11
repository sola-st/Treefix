from flask import Response, jsonify # pragma: no cover

class MockApp(object): pass # pragma: no cover
self = type('Mock', (object,), {'_app': MockApp(), 'dumps': lambda x: json.dumps(x), '_prepare_response_obj': lambda y, z: {'args': y, 'kwargs': z} })() # pragma: no cover
args = (1, 2, 3) # pragma: no cover
kwargs = {'key': 'value'} # pragma: no cover

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
