import click # pragma: no cover

_env_file_option = click.Option(['--env-file'], help='Path to the environment file') # pragma: no cover
_debug_option = click.Option(['--debug'], help='Enable debug mode') # pragma: no cover
version_option = click.Option(['--version'], is_flag=True, help='Show the version') # pragma: no cover
extra = {} # pragma: no cover
add_version_option = True # pragma: no cover
add_default_commands = True # pragma: no cover
create_app = lambda: print('create_app called') # pragma: no cover
load_dotenv = lambda: print('load_dotenv called') # pragma: no cover
set_debug_flag = lambda: print('set_debug_flag called') # pragma: no cover
run_command = click.Command('run', callback=lambda: print('run_command called')) # pragma: no cover
shell_command = click.Command('shell', callback=lambda: print('shell_command called')) # pragma: no cover
routes_command = click.Command('routes', callback=lambda: print('routes_command called')) # pragma: no cover
class MockSuper: # pragma: no cover
    def __init__(self, params, **extra): # pragma: no cover
        print(f'Super init called with params: {params}, extra: {extra}') # pragma: no cover
    def add_command(self, cmd): # pragma: no cover
        cmd.callback() # pragma: no cover
params = list(extra.pop('params', None) or ()) # pragma: no cover
params.extend((_env_file_option, _app_option, _debug_option)) # pragma: no cover
if add_version_option: # pragma: no cover
    params.append(version_option) # pragma: no cover
if 'context_settings' not in extra: # pragma: no cover
    extra['context_settings'] = {} # pragma: no cover
extra['context_settings'].setdefault('auto_envvar_prefix', 'FLASK') # pragma: no cover
if add_default_commands: # pragma: no cover
    pass

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
params = list(extra.pop("params", None) or ())
_l_(18962)
# Processing is done with option callbacks instead of a group
# callback. This allows users to make a custom group callback
# without losing the behavior. --env-file must come first so
# that it is eagerly evaluated before --app.
params.extend((_env_file_option, _app_option, _debug_option))
_l_(18963)

if add_version_option:
    _l_(18965)

    params.append(version_option)
    _l_(18964)

if "context_settings" not in extra:
    _l_(18967)

    extra["context_settings"] = {}
    _l_(18966)

extra["context_settings"].setdefault("auto_envvar_prefix", "FLASK")
_l_(18968)

super().__init__(params=params, **extra)
_l_(18969)

self.create_app = create_app
_l_(18970)
self.load_dotenv = load_dotenv
_l_(18971)
self.set_debug_flag = set_debug_flag
_l_(18972)

if add_default_commands:
    _l_(18976)

    self.add_command(run_command)
    _l_(18973)
    self.add_command(shell_command)
    _l_(18974)
    self.add_command(routes_command)
    _l_(18975)

self._loaded_plugin_commands = False
_l_(18977)
