import re # pragma: no cover
from flask import Flask # pragma: no cover
from werkzeug.utils import import_string as prepare_import # pragma: no cover

class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._loaded_app = None # pragma: no cover
        self.create_app = None # pragma: no cover
        self.set_debug_flag = False # pragma: no cover
mock_self = MockSelf() # pragma: no cover
        return Flask(name if name else __name__) # pragma: no cover
    if raise_if_not_found: # pragma: no cover
        raise NoAppException('App not found') # pragma: no cover
    return None # pragma: no cover
def get_debug_flag(): # pragma: no cover
    return True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Loads the Flask app (if not yet loaded) and returns it.  Calling
        this multiple times will just result in the already loaded app to
        be returned.
        """
if self._loaded_app is not None:
    _l_(20518)

    aux = self._loaded_app
    _l_(20517)
    exit(aux)

if self.create_app is not None:
    _l_(20529)

    app = self.create_app()
    _l_(20519)
else:
    if self.app_import_path:
        _l_(20528)

        path, name = (
            re.split(r":(?![\\/])", self.app_import_path, 1) + [None]
        )[:2]
        _l_(20520)
        import_name = prepare_import(path)
        _l_(20521)
        app = locate_app(import_name, name)
        _l_(20522)
    else:
        for path in ("wsgi.py", "app.py"):
            _l_(20527)

            import_name = prepare_import(path)
            _l_(20523)
            app = locate_app(import_name, None, raise_if_not_found=False)
            _l_(20524)

            if app:
                _l_(20526)

                break
                _l_(20525)

if not app:
    _l_(20531)

    raise NoAppException(
        "Could not locate a Flask application. Use the"
        " 'flask --app' option, 'FLASK_APP' environment"
        " variable, or a 'wsgi.py' or 'app.py' file in the"
        " current directory."
    )
    _l_(20530)

if self.set_debug_flag:
    _l_(20533)

    # Update the app's debug flag through the descriptor so that
    # other values repopulate as well.
    app.debug = get_debug_flag()
    _l_(20532)

self._loaded_app = app
_l_(20534)
aux = app
_l_(20535)
exit(aux)
