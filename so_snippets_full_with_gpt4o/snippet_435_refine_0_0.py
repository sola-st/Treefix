command = 'start' # pragma: no cover

import types # pragma: no cover
import sys # pragma: no cover

module_name = 'myapp.commands.start' # pragma: no cover
command = 'start' # pragma: no cover
module = types.ModuleType(module_name) # pragma: no cover
sys.modules[module_name] = module # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/301134/how-can-i-import-a-module-dynamically-given-its-name-as-string
from l3.Runtime import _l_
exec("import myapp.commands.%s" % command)
_l_(13303)

