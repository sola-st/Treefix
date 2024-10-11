command = 'example_command' # pragma: no cover

import types # pragma: no cover
import sys # pragma: no cover

command = 'example_command' # pragma: no cover
sys.modules['myapp.commands'] = types.ModuleType('myapp.commands') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/301134/how-can-i-import-a-module-dynamically-given-its-name-as-string
from l3.Runtime import _l_
exec("import myapp.commands.%s" % command)
_l_(1599)

