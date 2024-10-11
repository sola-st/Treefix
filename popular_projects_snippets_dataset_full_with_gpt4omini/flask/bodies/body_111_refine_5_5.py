import os # pragma: no cover
import sys # pragma: no cover
import click # pragma: no cover
from typing import Dict, Any # pragma: no cover
from werkzeug.serving import run_simple # pragma: no cover

is_running_from_reloader = lambda: False # pragma: no cover
get_load_dotenv = lambda x: x # pragma: no cover
load_dotenv = True # pragma: no cover
cli = type('MockCLI', (), {'load_dotenv': lambda: None, 'show_server_banner': lambda debug, name: None})() # pragma: no cover
self = type('MockApp', (), {'config': {'SERVER_NAME': None}, 'debug': False, '_got_first_request': True, 'name': 'MockApp'})() # pragma: no cover
get_debug_flag = lambda: True # pragma: no cover
debug = None # pragma: no cover
host = None # pragma: no cover
port = None # pragma: no cover
options = {} # pragma: no cover
t = type('MockType', (), {'cast': lambda x, y: x})() # pragma: no cover

import os # pragma: no cover
import sys # pragma: no cover
import click # pragma: no cover
from typing import Dict, Any # pragma: no cover
from werkzeug.serving import run_simple # pragma: no cover

is_running_from_reloader = lambda: False # pragma: no cover
def get_load_dotenv(value): return value # pragma: no cover
load_dotenv = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Runs the application on a local development server.

        Do not use ``run()`` in a production setting. It is not intended to
        meet security and performance requirements for a production server.
        Instead, see :doc:`/deploying/index` for WSGI server recommendations.

        If the :attr:`debug` flag is set the server will automatically reload
        for code changes and show a debugger in case an exception happened.

        If you want to run the application in debug mode, but disable the
        code execution on the interactive debugger, you can pass
        ``use_evalex=False`` as parameter.  This will keep the debugger's
        traceback screen active, but disable code execution.

        It is not recommended to use this function for development with
        automatic reloading as this is badly supported.  Instead you should
        be using the :command:`flask` command line script's ``run`` support.

        .. admonition:: Keep in Mind

           Flask will suppress any server error with a generic error page
           unless it is in debug mode.  As such to enable just the
           interactive debugger without the code reloading, you have to
           invoke :meth:`run` with ``debug=True`` and ``use_reloader=False``.
           Setting ``use_debugger`` to ``True`` without being in debug mode
           won't catch any exceptions because there won't be any to
           catch.

        :param host: the hostname to listen on. Set this to ``'0.0.0.0'`` to
            have the server available externally as well. Defaults to
            ``'127.0.0.1'`` or the host in the ``SERVER_NAME`` config variable
            if present.
        :param port: the port of the webserver. Defaults to ``5000`` or the
            port defined in the ``SERVER_NAME`` config variable if present.
        :param debug: if given, enable or disable debug mode. See
            :attr:`debug`.
        :param load_dotenv: Load the nearest :file:`.env` and :file:`.flaskenv`
            files to set environment variables. Will also change the working
            directory to the directory containing the first file found.
        :param options: the options to be forwarded to the underlying Werkzeug
            server. See :func:`werkzeug.serving.run_simple` for more
            information.

        .. versionchanged:: 1.0
            If installed, python-dotenv will be used to load environment
            variables from :file:`.env` and :file:`.flaskenv` files.

            The :envvar:`FLASK_DEBUG` environment variable will override :attr:`debug`.

            Threaded mode is enabled by default.

        .. versionchanged:: 0.10
            The default port is now picked from the ``SERVER_NAME``
            variable.
        """
# Ignore this call so that it doesn't start another server if
# the 'flask run' command is used.
if os.environ.get("FLASK_RUN_FROM_CLI") == "true":
    _l_(5609)

    if not is_running_from_reloader():
        _l_(5607)

        click.secho(
            " * Ignoring a call to 'app.run()' that would block"
            " the current 'flask' CLI command.\n"
            "   Only call 'app.run()' in an 'if __name__ =="
            ' "__main__"\' guard.',
            fg="red",
        )
        _l_(5606)

    exit()
    _l_(5608)

if get_load_dotenv(load_dotenv):
    _l_(5617)

    cli.load_dotenv()
    _l_(5610)

    # if set, let env vars override previous values
    if "FLASK_ENV" in os.environ:
        _l_(5616)

        print(
            "'FLASK_ENV' is deprecated and will not be used in"
            " Flask 2.3. Use 'FLASK_DEBUG' instead.",
            file=sys.stderr,
        )
        _l_(5611)
        self.config["ENV"] = os.environ.get("FLASK_ENV") or "production"
        _l_(5612)
        self.debug = get_debug_flag()
        _l_(5613)
    elif "FLASK_DEBUG" in os.environ:
        _l_(5615)

        self.debug = get_debug_flag()
        _l_(5614)
if debug is not None:
    _l_(5619)

    self.debug = bool(debug)
    _l_(5618)

server_name = self.config.get("SERVER_NAME")
_l_(5620)
sn_host = sn_port = None
_l_(5621)

if server_name:
    _l_(5623)

    sn_host, _, sn_port = server_name.partition(":")
    _l_(5622)

if not host:
    _l_(5627)

    if sn_host:
        _l_(5626)

        host = sn_host
        _l_(5624)
    else:
        host = "127.0.0.1"
        _l_(5625)

if port or port == 0:
    _l_(5632)

    port = int(port)
    _l_(5628)
elif sn_port:
    _l_(5631)

    port = int(sn_port)
    _l_(5629)
else:
    port = 5000
    _l_(5630)

options.setdefault("use_reloader", self.debug)
_l_(5633)
options.setdefault("use_debugger", self.debug)
_l_(5634)
options.setdefault("threaded", True)
_l_(5635)

cli.show_server_banner(self.debug, self.name)
_l_(5636)
try:
    from werkzeug.serving import run_simple
    _l_(5638)

except ImportError:
    pass

try:
    _l_(5642)

    run_simple(t.cast(str, host), port, self, **options)
    _l_(5639)
finally:
    _l_(5641)

    # reset the first request information if the development server
    # reset normally.  This makes it possible to restart the server
    # without reloader and that stuff from an interactive shell.
    self._got_first_request = False
    _l_(5640)
