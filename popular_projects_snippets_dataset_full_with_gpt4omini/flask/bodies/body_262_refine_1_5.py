from typing import Dict, List, Any, Optional # pragma: no cover

extra = {'params': []} # pragma: no cover
_env_file_option = '--env-file' # pragma: no cover
_app_option = '--app' # pragma: no cover
_debug_option = '--debug' # pragma: no cover
add_version_option = True # pragma: no cover
version_option = '--version' # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
create_app = lambda: 'app created' # pragma: no cover
load_dotenv = lambda: 'dotenv loaded' # pragma: no cover
set_debug_flag = lambda flag: 'debug set to ' + str(flag) # pragma: no cover
add_default_commands = True # pragma: no cover
run_command = 'run command' # pragma: no cover
shell_command = 'shell command' # pragma: no cover
routes_command = 'routes command' # pragma: no cover

from typing import Dict, List, Any, Optional # pragma: no cover

extra = {'params': []} # pragma: no cover
_env_file_option = '--env-file' # pragma: no cover
_app_option = '--app' # pragma: no cover
_debug_option = '--debug' # pragma: no cover
add_version_option = True # pragma: no cover
version_option = '--version' # pragma: no cover
class MockBase: pass # pragma: no cover
self = type('Mock', (MockBase,), {'create_app': None, 'load_dotenv': None, 'set_debug_flag': None, 'add_command': lambda self, cmd: None, '_loaded_plugin_commands': False})() # pragma: no cover
create_app = lambda: 'app created' # pragma: no cover
load_dotenv = lambda: 'dotenv loaded' # pragma: no cover
set_debug_flag = lambda flag: 'debug set to ' + str(flag) # pragma: no cover
add_default_commands = True # pragma: no cover
run_command = 'run command' # pragma: no cover
shell_command = 'shell command' # pragma: no cover
routes_command = 'routes command' # pragma: no cover

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
