from types import SimpleNamespace # pragma: no cover

cli = SimpleNamespace(main=lambda: print('cli.main called')) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
cli.main()
_l_(22563)
