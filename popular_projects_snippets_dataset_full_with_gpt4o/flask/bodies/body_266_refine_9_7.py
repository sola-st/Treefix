import os # pragma: no cover
from dotenv import load_dotenv # pragma: no cover
from typing import Any, Callable # pragma: no cover

def get_load_dotenv(load_dotenv: bool) -> bool:# pragma: no cover
    return True # pragma: no cover
class MockSelf:# pragma: no cover
    load_dotenv = True# pragma: no cover
    context_settings = {}# pragma: no cover
    def create_app(self) -> None:# pragma: no cover
        pass# pragma: no cover
    def set_debug_flag(self) -> None:# pragma: no cover
        pass # pragma: no cover
self = MockSelf() # pragma: no cover
extra = {} # pragma: no cover
class ScriptInfo:# pragma: no cover
    def __init__(self, create_app: Callable[[], None], set_debug_flag: Callable[[], None]):# pragma: no cover
        self.create_app = create_app# pragma: no cover
        self.set_debug_flag = set_debug_flag # pragma: no cover
info_name = "default_info" # pragma: no cover
args = [] # pragma: no cover
parent = None # pragma: no cover

import os # pragma: no cover
from dotenv import load_dotenv # pragma: no cover
from typing import Any, Dict, Callable # pragma: no cover

def get_load_dotenv(load_dotenv: bool) -> bool:# pragma: no cover
    return load_dotenv # pragma: no cover
class MockSelfParent:# pragma: no cover
    def make_context(self, info_name: str, args: list, parent: Any = None, **extra: Dict[str, Any]) -> Dict[str, Any]:# pragma: no cover
        return { 'info_name': info_name, 'args': args, 'parent': parent, **extra } # pragma: no cover
class MockSelf(MockSelfParent):# pragma: no cover
    load_dotenv = True# pragma: no cover
    context_settings = {}# pragma: no cover
    def create_app(self) -> None:# pragma: no cover
        pass# pragma: no cover
    def set_debug_flag(self) -> None:# pragma: no cover
        pass # pragma: no cover
self = MockSelf() # pragma: no cover
extra = {} # pragma: no cover
class ScriptInfo:# pragma: no cover
    def __init__(self, create_app: Callable[[], None], set_debug_flag: Callable[[], None]):# pragma: no cover
        self.create_app = create_app# pragma: no cover
        self.set_debug_flag = set_debug_flag # pragma: no cover
info_name = "default_info" # pragma: no cover
args = [] # pragma: no cover
parent = None # pragma: no cover

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
