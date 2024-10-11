from flask import Flask, send_from_directory # pragma: no cover
import werkzeug.utils # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.config['UPLOAD_FOLDER'] = './uploads' # pragma: no cover
directory = app.config['UPLOAD_FOLDER'] # pragma: no cover
path = 'example.txt' # pragma: no cover
_prepare_send_file_kwargs = lambda **kwargs: kwargs # pragma: no cover
kwargs = {'Cache-Control': 'no-cache'} # pragma: no cover

from flask import Flask, send_from_directory, request # pragma: no cover
import werkzeug.utils # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.config['UPLOAD_FOLDER'] = './uploads' # pragma: no cover
directory = app.config['UPLOAD_FOLDER'] # pragma: no cover
path = 'example.txt' # pragma: no cover
_prepare_send_file_kwargs = lambda **kwargs: kwargs # pragma: no cover
kwargs = {} # pragma: no cover
app.route('/uploads/<path:name>')(lambda name: send_from_directory(directory, name, **_prepare_send_file_kwargs(**kwargs))) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
"""Send a file from within a directory using :func:`send_file`.

    .. code-block:: python

        @app.route("/uploads/<path:name>")
        def download_file(name):
            return send_from_directory(
                app.config['UPLOAD_FOLDER'], name, as_attachment=True
            )

    This is a secure way to serve files from a folder, such as static
    files or uploads. Uses :func:`~werkzeug.security.safe_join` to
    ensure the path coming from the client is not maliciously crafted to
    point outside the specified directory.

    If the final path does not point to an existing regular file,
    raises a 404 :exc:`~werkzeug.exceptions.NotFound` error.

    :param directory: The directory that ``path`` must be located under,
        relative to the current application's root path.
    :param path: The path to the file to send, relative to
        ``directory``.
    :param kwargs: Arguments to pass to :func:`send_file`.

    .. versionchanged:: 2.0
        ``path`` replaces the ``filename`` parameter.

    .. versionadded:: 2.0
        Moved the implementation to Werkzeug. This is now a wrapper to
        pass some Flask-specific arguments.

    .. versionadded:: 0.5
    """
aux = werkzeug.utils.send_from_directory(  # type: ignore[return-value]
    directory, path, **_prepare_send_file_kwargs(**kwargs)
)
_l_(8239)
exit(aux)
