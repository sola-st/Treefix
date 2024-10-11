import re # pragma: no cover
from flask import Flask # pragma: no cover
from werkzeug.exceptions import HTTPException # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._loaded_app = None # pragma: no cover
self.create_app = None # pragma: no cover
self.set_debug_flag = False # pragma: no cover
class NoAppException(Exception): pass # pragma: no cover
def get_debug_flag(): return True # pragma: no cover

import re # pragma: no cover
from flask import Flask # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._loaded_app = None # pragma: no cover
self.create_app = None # pragma: no cover
self.set_debug_flag = False # pragma: no cover
class NoAppException(Exception): pass # pragma: no cover
def get_debug_flag(): return True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Loads the Flask app (if not yet loaded) and returns it.  Calling
        this multiple times will just result in the already loaded app to
        be returned.
        """
if self._loaded_app is not None:
    _l_(9364)

    aux = self._loaded_app
    _l_(9363)
    exit(aux)

if self.create_app is not None:
    _l_(9375)

    app = self.create_app()
    _l_(9365)
else:
    if self.app_import_path:
        _l_(9374)

        path, name = (
            re.split(r":(?![\\/])", self.app_import_path, 1) + [None]
        )[:2]
        _l_(9366)
        import_name = prepare_import(path)
        _l_(9367)
        app = locate_app(import_name, name)
        _l_(9368)
    else:
        for path in ("wsgi.py", "app.py"):
            _l_(9373)

            import_name = prepare_import(path)
            _l_(9369)
            app = locate_app(import_name, None, raise_if_not_found=False)
            _l_(9370)

            if app:
                _l_(9372)

                break
                _l_(9371)

if not app:
    _l_(9377)

    raise NoAppException(
        "Could not locate a Flask application. Use the"
        " 'flask --app' option, 'FLASK_APP' environment"
        " variable, or a 'wsgi.py' or 'app.py' file in the"
        " current directory."
    )
    _l_(9376)

if self.set_debug_flag:
    _l_(9379)

    # Update the app's debug flag through the descriptor so that
    # other values repopulate as well.
    app.debug = get_debug_flag()
    _l_(9378)

self._loaded_app = app
_l_(9380)
aux = app
_l_(9381)
exit(aux)
