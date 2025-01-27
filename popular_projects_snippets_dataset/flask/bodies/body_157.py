# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""The WSGI server calls the Flask application object as the
        WSGI application. This calls :meth:`wsgi_app`, which can be
        wrapped to apply middleware.
        """
aux = self.wsgi_app(environ, start_response)
_l_(19672)
exit(aux)
