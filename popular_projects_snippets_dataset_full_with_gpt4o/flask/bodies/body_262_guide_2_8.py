import click # pragma: no cover

_env_file_option = click.Option(['--env-file'], help='Environment file') # pragma: no cover
_app_option = click.Option(['--app'], help='App option') # pragma: no cover
_debug_option = click.Option(['--debug'], help='Debug option') # pragma: no cover
version_option = click.Option(['--version'], help='Version option') # pragma: no cover
create_app = lambda: print('create_app called') # pragma: no cover
load_dotenv = lambda: print('load_dotenv called') # pragma: no cover
set_debug_flag = lambda: print('set_debug_flag called') # pragma: no cover
run_command = click.Command('run', callback=lambda: print('run_command executed')) # pragma: no cover
shell_command = click.Command('shell', callback=lambda: print('shell_command executed')) # pragma: no cover
routes_command = click.Command('routes', callback=lambda: print('routes_command executed')) # pragma: no cover
add_version_option = True # pragma: no cover
extra = {} # pragma: no cover
add_default_commands = True # pragma: no cover
class MockSuperClass: # pragma: no cover
    def __init__(self, params, **extra): # pragma: no cover
        print('MockSuperClass init called with:', params, extra) # pragma: no cover
    def add_command(self, command): # pragma: no cover
        command.callback() # pragma: no cover

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
