import click # pragma: no cover
from flask import Flask # pragma: no cover

class MockSuperClass: # pragma: no cover
    def __init__(self, params=None, **extra): # pragma: no cover
        pass # pragma: no cover
create_app = Flask(__name__) # pragma: no cover
load_dotenv = lambda: None # pragma: no cover
set_debug_flag = lambda: None # pragma: no cover
run_command = click.Command('run') # pragma: no cover
shell_command = click.Command('shell') # pragma: no cover
routes_command = click.Command('routes') # pragma: no cover
version_option = click.Option(['--version']) # pragma: no cover
_env_file_option = click.Option(['--env-file']) # pragma: no cover
_app_option = click.Option(['--app']) # pragma: no cover
_debug_option = click.Option(['--debug']) # pragma: no cover
extra = {} # pragma: no cover
add_version_option = True # pragma: no cover
add_default_commands = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
params = list(extra.pop("params", None) or ())
_l_(18916)
# Processing is done with option callbacks instead of a group
# callback. This allows users to make a custom group callback
# without losing the behavior. --env-file must come first so
# that it is eagerly evaluated before --app.
params.extend((_env_file_option, _app_option, _debug_option))
_l_(18917)

if add_version_option:
    _l_(18919)

    params.append(version_option)
    _l_(18918)

if "context_settings" not in extra:
    _l_(18921)

    extra["context_settings"] = {}
    _l_(18920)

extra["context_settings"].setdefault("auto_envvar_prefix", "FLASK")
_l_(18922)

super().__init__(params=params, **extra)
_l_(18923)

self.create_app = create_app
_l_(18924)
self.load_dotenv = load_dotenv
_l_(18925)
self.set_debug_flag = set_debug_flag
_l_(18926)

if add_default_commands:
    _l_(18930)

    self.add_command(run_command)
    _l_(18927)
    self.add_command(shell_command)
    _l_(18928)
    self.add_command(routes_command)
    _l_(18929)

self._loaded_plugin_commands = False
_l_(18931)
