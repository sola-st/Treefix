import os # pragma: no cover
from dotenv import load_dotenv # pragma: no cover
from typing import Any, Dict, List, Tuple # pragma: no cover

def get_load_dotenv(flag: Any) -> bool: return bool(flag) # pragma: no cover
extra: Dict[str, Any] = {} # pragma: no cover
class ScriptInfo:# pragma: no cover
    def __init__(self, create_app: Any, set_debug_flag: Any):# pragma: no cover
        self.create_app = create_app# pragma: no cover
        self.set_debug_flag = set_debug_flag # pragma: no cover
info_name: str = 'sample_info' # pragma: no cover
args: List[str] = [] # pragma: no cover
parent: Any = None # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    'load_dotenv': True, # pragma: no cover
    'context_settings': {}, # pragma: no cover
    'create_app': lambda: None, # pragma: no cover
    'set_debug_flag': lambda: None,# pragma: no cover
    'make_context': lambda *args, **kwargs: None# pragma: no cover
})() # pragma: no cover

import os # pragma: no cover
from dotenv import load_dotenv # pragma: no cover
from typing import Any, Dict, List # pragma: no cover

def get_load_dotenv(flag: Any) -> bool: return bool(flag) # pragma: no cover
class MockBase:# pragma: no cover
    def make_context(self, info_name: str, args: List[str], parent: Any, **extra: Any) -> None:# pragma: no cover
        pass # pragma: no cover
self = type('Mock', (MockBase,), {# pragma: no cover
    'load_dotenv': True, # pragma: no cover
    'context_settings': {}, # pragma: no cover
    'create_app': lambda: None, # pragma: no cover
    'set_debug_flag': lambda: None# pragma: no cover
})() # pragma: no cover
extra: Dict[str, Any] = {} # pragma: no cover
class ScriptInfo:# pragma: no cover
    def __init__(self, create_app: Any, set_debug_flag: Any) -> None:# pragma: no cover
        self.create_app = create_app# pragma: no cover
        self.set_debug_flag = set_debug_flag # pragma: no cover
info_name: str = 'example_info_name' # pragma: no cover
args: List[str] = [] # pragma: no cover
parent: Any = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
# Set a flag to tell app.run to become a no-op. If app.run was
# not in a __name__ == __main__ guard, it would start the server
# when importing, blocking whatever command is being called.
from l3.Runtime import _l_
os.environ["FLASK_RUN_FROM_CLI"] = "true"
_l_(22988)

# Attempt to load .env and .flask env files. The --env-file
# option can cause another file to be loaded.
if get_load_dotenv(self.load_dotenv):
    _l_(22990)

    load_dotenv()
    _l_(22989)

if "obj" not in extra and "obj" not in self.context_settings:
    _l_(22992)

    extra["obj"] = ScriptInfo(
        create_app=self.create_app, set_debug_flag=self.set_debug_flag
    )
    _l_(22991)
aux = super().make_context(info_name, args, parent=parent, **extra)
_l_(22993)

exit(aux)
