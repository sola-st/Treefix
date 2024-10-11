from unittest.mock import Mock # pragma: no cover

extra = {'context_settings': {'auto_envvar_prefix': 'FLASK'}} # pragma: no cover
_env_file_option = '--env-file' # pragma: no cover
_app_option = '--app' # pragma: no cover
_debug_option = '--debug' # pragma: no cover
add_version_option = False # pragma: no cover
version_option = '--version' # pragma: no cover
self = Mock(create_app=Mock(), load_dotenv=Mock(), set_debug_flag=Mock(), add_command=Mock()) # pragma: no cover
create_app = Mock() # pragma: no cover
load_dotenv = Mock() # pragma: no cover
set_debug_flag = Mock() # pragma: no cover
add_default_commands = False # pragma: no cover
run_command = Mock() # pragma: no cover
shell_command = Mock() # pragma: no cover
routes_command = Mock() # pragma: no cover

from unittest.mock import Mock # pragma: no cover

class BaseClass:# pragma: no cover
    def __init__(self, params=None, **kwargs):# pragma: no cover
        pass # pragma: no cover
class DerivedClass(BaseClass):# pragma: no cover
    def __init__(self, params=None, **kwargs):# pragma: no cover
        super().__init__(params=params, **kwargs) # pragma: no cover
extra = {'context_settings': {'auto_envvar_prefix': 'FLASK'}} # pragma: no cover
_env_file_option = '--env-file' # pragma: no cover
_app_option = '--app' # pragma: no cover
_debug_option = '--debug' # pragma: no cover
add_version_option = True # pragma: no cover
version_option = '--version' # pragma: no cover
self = DerivedClass() # pragma: no cover
self.create_app = Mock() # pragma: no cover
self.load_dotenv = Mock() # pragma: no cover
self.set_debug_flag = Mock() # pragma: no cover
add_default_commands = True # pragma: no cover
run_command = Mock(name='run') # pragma: no cover
shell_command = Mock(name='shell') # pragma: no cover
routes_command = Mock(name='routes') # pragma: no cover

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
