from flask import Flask, Response # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = type('Mock', (object,), {'wsgi_app': app.wsgi_app})() # pragma: no cover
environ = {'REQUEST_METHOD': 'GET', 'PATH_INFO': '/', 'wsgi.version': (1, 0), 'wsgi.url_scheme': 'http', 'SERVER_NAME': 'localhost', 'SERVER_PORT': '5000', 'wsgi.input': '', 'wsgi.errors': '', 'SCRIPT_NAME': ''} # pragma: no cover
def start_response(status, headers): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""The WSGI server calls the Flask application object as the
        WSGI application. This calls :meth:`wsgi_app`, which can be
        wrapped to apply middleware.
        """
aux = self.wsgi_app(environ, start_response)
_l_(8559)
exit(aux)
