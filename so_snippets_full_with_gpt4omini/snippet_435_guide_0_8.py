command = 'example_command' # pragma: no cover
mock_command_module = type('Mock', (object,), {'example_command': lambda: 'Executed example_command'}) # pragma: no cover
myapp = type('MockApp', (object,), {'commands': {'example_command': mock_command_module}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/301134/how-can-i-import-a-module-dynamically-given-its-name-as-string
from l3.Runtime import _l_
exec("import myapp.commands.%s" % command)
_l_(1599)

