import sys # pragma: no cover
import os # pragma: no cover
import types # pragma: no cover

sys.version = '3.9.1 (default, Dec  8 2020, 07:51:42) \n[GCC 7.3.0]' # pragma: no cover
sys.platform = 'linux' # pragma: no cover
os.environ = {'PYTHONSTARTUP': '/home/user/.pythonstartup'} # pragma: no cover
os.path = type('MockPath', (), {'isfile': lambda x: True})() # pragma: no cover

import sys # pragma: no cover
import os # pragma: no cover
import types # pragma: no cover

class CurrentAppMock:# pragma: no cover
    instance_path = '/path/to/instance'# pragma: no cover
    def make_shell_context(self):# pragma: no cover
        return {} # pragma: no cover
current_app = CurrentAppMock() # pragma: no cover
sys.version = '3.9.1 (default, Dec  8 2020, 07:51:42) \n[GCC 7.3.0]' # pragma: no cover
sys.platform = 'linux' # pragma: no cover
os.environ = {'PYTHONSTARTUP': ''} # pragma: no cover
os.path = type('MockPath', (object,), {'isfile': lambda x: False})() # pragma: no cover

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
    _l_(17393)

except ImportError:
    pass

banner = (
    f"Python {sys.version} on {sys.platform}\n"
    f"App: {current_app.import_name}\n"
    f"Instance: {current_app.instance_path}"
)
_l_(17394)
ctx: dict = {}
_l_(17395)

# Support the regular Python interpreter startup script if someone
# is using it.
startup = os.environ.get("PYTHONSTARTUP")
_l_(17396)
if startup and os.path.isfile(startup):
    _l_(17399)

    with open(startup) as f:
        _l_(17398)

        eval(compile(f.read(), startup, "exec"), ctx)
        _l_(17397)

ctx.update(current_app.make_shell_context())
_l_(17400)

# Site, customize, or startup script can set a hook to call when
# entering interactive mode. The default one sets up readline with
# tab and history completion.
interactive_hook = getattr(sys, "__interactivehook__", None)
_l_(17401)

if interactive_hook is not None:
    _l_(17409)

    try:
        _l_(17407)

        import readline
        _l_(17402)
        from rlcompleter import Completer
        _l_(17403)
    except ImportError:
        _l_(17405)

        pass
        _l_(17404)
    else:
        # rlcompleter uses __main__.__dict__ by default, which is
        # flask.__main__. Use the shell context instead.
        readline.set_completer(Completer(ctx).complete)
        _l_(17406)

    interactive_hook()
    _l_(17408)

code.interact(banner=banner, local=ctx)
_l_(17410)
