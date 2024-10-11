from flask import Flask # pragma: no cover
from dotenv import load_dotenv # pragma: no cover
import click # pragma: no cover

extra = {'params': [], 'context_settings': {}} # pragma: no cover
_env_file_option = click.Option(['--env-file'], help='Path to the environment file.') # pragma: no cover
_app_option = click.Option(['--app'], help='Specify the application to load.') # pragma: no cover
_debug_option = click.Option(['--debug'], is_flag=True, help='Run in debug mode.') # pragma: no cover
add_version_option = False # pragma: no cover
version_option = click.Option(['--version'], is_flag=True, help='Show the version.') # pragma: no cover
self = type('Mock', (object,), {'create_app': None, 'load_dotenv': load_dotenv, 'set_debug_flag': None, 'add_command': lambda self, cmd: None, '_loaded_plugin_commands': False})() # pragma: no cover
create_app = Flask(__name__) # pragma: no cover
load_dotenv = load_dotenv # pragma: no cover
set_debug_flag = lambda flag: None # pragma: no cover
add_default_commands = False # pragma: no cover
run_command = click.Command('run', help='Run the application.') # pragma: no cover
shell_command = click.Command('shell', help='Start a shell.') # pragma: no cover
routes_command = click.Command('routes', help='Show the registered routes.') # pragma: no cover

from flask import Flask # pragma: no cover
import click # pragma: no cover
from dotenv import load_dotenv # pragma: no cover

class Base: pass # pragma: no cover
extra = {'params': []} # pragma: no cover
_env_file_option = click.Option(['--env-file'], help='Path to the environment file.') # pragma: no cover
_app_option = click.Option(['--app'], help='Specify the application to load.') # pragma: no cover
_debug_option = click.Option(['--debug'], is_flag=True, help='Run in debug mode.') # pragma: no cover
add_version_option = True # pragma: no cover
version_option = click.Option(['--version'], is_flag=True, help='Show the version.') # pragma: no cover
self = type('Mock', (Base,), {'create_app': None, 'load_dotenv': load_dotenv, 'set_debug_flag': None, 'add_command': lambda self, cmd: None, '_loaded_plugin_commands': False})() # pragma: no cover
create_app = Flask(__name__) # pragma: no cover
load_dotenv = load_dotenv # pragma: no cover
set_debug_flag = lambda flag: None # pragma: no cover
add_default_commands = True # pragma: no cover
run_command = click.Command('run', help='Run the application.') # pragma: no cover
shell_command = click.Command('shell', help='Start a shell.') # pragma: no cover
routes_command = click.Command('routes', help='Show the registered routes.') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
params = list(extra.pop("params", None) or ())
_l_(7717)
# Processing is done with option callbacks instead of a group
# callback. This allows users to make a custom group callback
# without losing the behavior. --env-file must come first so
# that it is eagerly evaluated before --app.
params.extend((_env_file_option, _app_option, _debug_option))
_l_(7718)

if add_version_option:
    _l_(7720)

    params.append(version_option)
    _l_(7719)

if "context_settings" not in extra:
    _l_(7722)

    extra["context_settings"] = {}
    _l_(7721)

extra["context_settings"].setdefault("auto_envvar_prefix", "FLASK")
_l_(7723)

super().__init__(params=params, **extra)
_l_(7724)

self.create_app = create_app
_l_(7725)
self.load_dotenv = load_dotenv
_l_(7726)
self.set_debug_flag = set_debug_flag
_l_(7727)

if add_default_commands:
    _l_(7731)

    self.add_command(run_command)
    _l_(7728)
    self.add_command(shell_command)
    _l_(7729)
    self.add_command(routes_command)
    _l_(7730)

self._loaded_plugin_commands = False
_l_(7732)
