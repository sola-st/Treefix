from markupsafe import Markup # pragma: no cover

value = 'Hello, World!' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = Markup(value)
_l_(22593)
exit(aux)
