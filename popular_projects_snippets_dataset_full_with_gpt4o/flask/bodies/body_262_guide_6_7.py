from click import Option, Command, Group # pragma: no cover

_env_file_option = Option(['--env-file'], help='Load environment from a .env file') # pragma: no cover
_app_option = Option(['--app'], help='The application to run') # pragma: no cover
_debug_option = Option(['--debug'], is_flag=True, help='Enable debug mode') # pragma: no cover
version_option = Option(['--version'], is_flag=True, help='Show the version and exit') # pragma: no cover
create_app = lambda: print('create_app executed') # pragma: no cover
load_dotenv = lambda: print('load_dotenv executed') # pragma: no cover
set_debug_flag = lambda: print('set_debug_flag executed') # pragma: no cover
run_command = Command('run', help='Run the application') # pragma: no cover
shell_command = Command('shell', help='Run a shell in the app context') # pragma: no cover
routes_command = Command('routes', help='Show the routes for the app') # pragma: no cover
params = [] # pragma: no cover
extra = {'context_settings': {}} # pragma: no cover
add_version_option = True # pragma: no cover
add_default_commands = True # pragma: no cover
class MockGroup(Group): # pragma: no cover
    def __init__(self, params=None, **extra): # pragma: no cover
        super().__init__(params=params, **extra) # pragma: no cover
    def add_command(self, cmd): # pragma: no cover
        print(f'Command {cmd.name} added') # pragma: no cover
 # pragma: no cover
mock_instance = MockGroup(params=params, **extra) # pragma: no cover
mock_instance.create_app = create_app # pragma: no cover
mock_instance.load_dotenv = load_dotenv # pragma: no cover
mock_instance.set_debug_flag = set_debug_flag # pragma: no cover
if add_default_commands: # pragma: no cover
    mock_instance.add_command(run_command) # pragma: no cover
    mock_instance.add_command(shell_command) # pragma: no cover
    mock_instance.add_command(routes_command) # pragma: no cover
mock_instance._loaded_plugin_commands = False # pragma: no cover

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
