import os # pragma: no cover
import click # pragma: no cover

def is_running_from_reloader(): # pragma: no cover
    return os.environ.get('WERKZEUG_RUN_MAIN') == 'true' # pragma: no cover
debug = True # pragma: no cover
click = type('Mock', (object,), { 'echo': lambda msg: print(msg) }) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Show extra startup messages the first time the server is run,
    ignoring the reloader.
    """
if is_running_from_reloader():
    _l_(19691)

    exit()
    _l_(19690)

if app_import_path is not None:
    _l_(19693)

    click.echo(f" * Serving Flask app '{app_import_path}'")
    _l_(19692)

if debug is not None:
    _l_(19695)

    click.echo(f" * Debug mode: {'on' if debug else 'off'}")
    _l_(19694)
