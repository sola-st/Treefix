from typing import Any # pragma: no cover
import typing as t # pragma: no cover
from flask import send_from_directory # pragma: no cover

self = type('Mock', (object,), {'has_static_folder': True, 'get_send_file_max_age': lambda self, filename: 3600, 'static_folder': '/path/to/static'})() # pragma: no cover
filename = 'example.txt' # pragma: no cover
t = type('Mock', (object,), {'cast': lambda _, type, value: value}) # pragma: no cover

import typing as t # pragma: no cover
from flask import send_from_directory, Flask # pragma: no cover

self = type('Mock', (object,), { # pragma: no cover
    'has_static_folder': True, # pragma: no cover
    'get_send_file_max_age': lambda self, filename: 3600, # pragma: no cover
    'static_folder': '/path/to/static' # pragma: no cover
})() # pragma: no cover
filename = 'example.txt' # pragma: no cover
t = type('Mock', (object,), {'cast': lambda self, type_, value: value}) # pragma: no cover
# Ensure there's an active app context to avoid errors # pragma: no cover
app = Flask(__name__) # pragma: no cover
ctx = app.app_context() # pragma: no cover
ctx.push() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""The view function used to serve files from
        :attr:`static_folder`. A route is automatically registered for
        this view at :attr:`static_url_path` if :attr:`static_folder` is
        set.

        .. versionadded:: 0.5
        """
if not self.has_static_folder:
    _l_(22670)

    raise RuntimeError("'static_folder' must be set to serve static_files.")
    _l_(22669)

# send_file only knows to call get_send_file_max_age on the app,
# call it here so it works for blueprints too.
max_age = self.get_send_file_max_age(filename)
_l_(22671)
aux = send_from_directory(
    t.cast(str, self.static_folder), filename, max_age=max_age
)
_l_(22672)
exit(aux)
