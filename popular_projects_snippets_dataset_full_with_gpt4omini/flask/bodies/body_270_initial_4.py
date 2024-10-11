from flask import Flask # pragma: no cover
import click # pragma: no cover

def is_running_from_reloader(): return False # pragma: no cover
click = type('MockClick', (object,), {'echo': print})() # pragma: no cover
debug = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Show extra startup messages the first time the server is run,
    ignoring the reloader.
    """
if is_running_from_reloader():
    _l_(8630)

    exit()
    _l_(8629)

if app_import_path is not None:
    _l_(8632)

    click.echo(f" * Serving Flask app '{app_import_path}'")
    _l_(8631)

if debug is not None:
    _l_(8634)

    click.echo(f" * Debug mode: {'on' if debug else 'off'}")
    _l_(8633)
