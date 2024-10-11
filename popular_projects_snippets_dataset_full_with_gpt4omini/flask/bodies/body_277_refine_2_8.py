import os # pragma: no cover
import sys # pragma: no cover
from flask import Flask, current_app # pragma: no cover

sys = type('Mock', (object,), {'version': '3.9.7', 'platform': 'linux'})( ) # pragma: no cover
os = type('Mock', (object,), {'environ': {}, 'path': type('Mock', (object,), {})})( ) # pragma: no cover

import os # pragma: no cover
import sys # pragma: no cover
from flask import Flask, current_app # pragma: no cover

sys = type('MockSys', (object,), {'version': '3.10.5', 'platform': 'linux'})() # pragma: no cover
app = Flask(__name__) # pragma: no cover
app.config['TESTING'] = True # pragma: no cover
current_app = app # pragma: no cover
current_app.instance_path = '/path/to/instance' # pragma: no cover
current_app.make_shell_context = lambda: {'app': current_app, 'some_var': 42} # pragma: no cover
os.environ = {'PYTHONSTARTUP': '/path/to/startup.py'} # pragma: no cover
os.path = type('MockPath', (object,), {'isfile': lambda self, path: path == '/path/to/startup.py'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Run an interactive Python shell in the context of a given
    Flask application.  The application will populate the default
    namespace of this shell according to its configuration.

    This is useful for executing small snippets of management code
    without having to manually configure the application.
    """
try:
    import code
    _l_(5644)

except ImportError:
    pass

banner = (
    f"Python {sys.version} on {sys.platform}\n"
    f"App: {current_app.import_name}\n"
    f"Instance: {current_app.instance_path}"
)
_l_(5645)
ctx: dict = {}
_l_(5646)

# Support the regular Python interpreter startup script if someone
# is using it.
startup = os.environ.get("PYTHONSTARTUP")
_l_(5647)
if startup and os.path.isfile(startup):
    _l_(5650)

    with open(startup) as f:
        _l_(5649)

        eval(compile(f.read(), startup, "exec"), ctx)
        _l_(5648)

ctx.update(current_app.make_shell_context())
_l_(5651)

# Site, customize, or startup script can set a hook to call when
# entering interactive mode. The default one sets up readline with
# tab and history completion.
interactive_hook = getattr(sys, "__interactivehook__", None)
_l_(5652)

if interactive_hook is not None:
    _l_(5660)

    try:
        _l_(5658)

        import readline
        _l_(5653)
        from rlcompleter import Completer
        _l_(5654)
    except ImportError:
        _l_(5656)

        pass
        _l_(5655)
    else:
        # rlcompleter uses __main__.__dict__ by default, which is
        # flask.__main__. Use the shell context instead.
        readline.set_completer(Completer(ctx).complete)
        _l_(5657)

    interactive_hook()
    _l_(5659)

code.interact(banner=banner, local=ctx)
_l_(5661)
