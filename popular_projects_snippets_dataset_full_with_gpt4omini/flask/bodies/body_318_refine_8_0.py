from flask import send_from_directory # pragma: no cover
import typing as t # pragma: no cover

class MockApp(object):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.has_static_folder = True# pragma: no cover
        self.static_folder = 'static'# pragma: no cover
    def get_send_file_max_age(self, filename):# pragma: no cover
        return 12 * 60 * 60  # 12 hours # pragma: no cover
self = MockApp() # pragma: no cover
filename = 'example.txt' # pragma: no cover
send_from_directory = send_from_directory # pragma: no cover

from flask import Flask, send_from_directory # pragma: no cover

app = Flask(__name__) # pragma: no cover
class MockApp:  # Mocking the app context# pragma: no cover
    def __init__(self):# pragma: no cover
        self.has_static_folder = True# pragma: no cover
        self.static_folder = '/path/to/static'# pragma: no cover
    def get_send_file_max_age(self, filename):# pragma: no cover
        return 3600 # pragma: no cover
self = MockApp() # pragma: no cover
filename = 'example.txt' # pragma: no cover
self.app = app # pragma: no cover

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
    _l_(5911)

    raise RuntimeError("'static_folder' must be set to serve static_files.")
    _l_(5910)

# send_file only knows to call get_send_file_max_age on the app,
# call it here so it works for blueprints too.
max_age = self.get_send_file_max_age(filename)
_l_(5912)
aux = send_from_directory(
    t.cast(str, self.static_folder), filename, max_age=max_age
)
_l_(5913)
exit(aux)
