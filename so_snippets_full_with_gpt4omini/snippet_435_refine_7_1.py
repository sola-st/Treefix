command = 'example_command' # pragma: no cover

import types # pragma: no cover

command = 'mock_command' # pragma: no cover
myapp = type('Mock', (object,), {'commands': types.ModuleType('mock_commands')}) # pragma: no cover
myapp.commands.mock_command = type('MockCommand', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/301134/how-can-i-import-a-module-dynamically-given-its-name-as-string
from l3.Runtime import _l_
exec("import myapp.commands.%s" % command)
_l_(1599)

