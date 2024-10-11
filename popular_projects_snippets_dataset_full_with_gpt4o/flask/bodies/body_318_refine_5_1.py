from typing import Any # pragma: no cover
import typing as t # pragma: no cover
from flask import send_from_directory # pragma: no cover

filename = 'example.txt' # pragma: no cover

from typing import Any # pragma: no cover
import typing as t # pragma: no cover
from flask import send_from_directory, Flask # pragma: no cover

class MockSelf: # pragma: no cover
    has_static_folder = True # pragma: no cover
    static_folder = '/path/to/static' # pragma: no cover
    def get_send_file_max_age(self, filename): # pragma: no cover
        return 3600 # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
filename = 'example.txt' # pragma: no cover
t = type('MockT', (object,), {'cast': lambda self, type_, value: value}) # pragma: no cover

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
