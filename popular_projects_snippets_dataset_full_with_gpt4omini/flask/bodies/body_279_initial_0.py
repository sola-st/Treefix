import types # pragma: no cover

cli = type('MockCLI', (object,), {'main': lambda self: 'CLI main method called'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
cli.main()
_l_(5078)
