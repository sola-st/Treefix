import sys # pragma: no cover
import os # pragma: no cover
import code # pragma: no cover
from flask import Flask, current_app # pragma: no cover
import readline # pragma: no cover
from rlcompleter import Completer # pragma: no cover

app = Flask(__name__) # pragma: no cover
ctx = app.app_context() # pragma: no cover
ctx.push() # pragma: no cover
current_app = type('Mock', (object,), { # pragma: no cover
    'instance_path': '/mock/instance/path', # pragma: no cover
    'make_shell_context': lambda: {'app': 'mock_app_context'} # pragma: no cover
})() # pragma: no cover
sys.version = '3.9.0 (default, Nov 6 2020, 10:49:32)' # pragma: no cover
sys.platform = 'linux' # pragma: no cover
startup_script = 'print(\'Running startup script\')' # pragma: no cover
os.environ['PYTHONSTARTUP'] = '/mock/startup.py' # pragma: no cover
os.path.isfile = lambda path: path == '/mock/startup.py' # pragma: no cover

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
    _l_(17339)

except ImportError:
    pass

banner = (
    f"Python {sys.version} on {sys.platform}\n"
    f"App: {current_app.import_name}\n"
    f"Instance: {current_app.instance_path}"
)
_l_(17340)
ctx: dict = {}
_l_(17341)

# Support the regular Python interpreter startup script if someone
# is using it.
startup = os.environ.get("PYTHONSTARTUP")
_l_(17342)
if startup and os.path.isfile(startup):
    _l_(17345)

    with open(startup) as f:
        _l_(17344)

        eval(compile(f.read(), startup, "exec"), ctx)
        _l_(17343)

ctx.update(current_app.make_shell_context())
_l_(17346)

# Site, customize, or startup script can set a hook to call when
# entering interactive mode. The default one sets up readline with
# tab and history completion.
interactive_hook = getattr(sys, "__interactivehook__", None)
_l_(17347)

if interactive_hook is not None:
    _l_(17355)

    try:
        _l_(17353)

        import readline
        _l_(17348)
        from rlcompleter import Completer
        _l_(17349)
    except ImportError:
        _l_(17351)

        pass
        _l_(17350)
    else:
        # rlcompleter uses __main__.__dict__ by default, which is
        # flask.__main__. Use the shell context instead.
        readline.set_completer(Completer(ctx).complete)
        _l_(17352)

    interactive_hook()
    _l_(17354)

code.interact(banner=banner, local=ctx)
_l_(17356)
