from typing import List # pragma: no cover

t = type('Mock', (object,), {'List': list}) # pragma: no cover
name = 'example.module.name' # pragma: no cover
_split_blueprint_path = lambda path: path.split('.') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
out: t.List[str] = [name]
_l_(4181)

if "." in name:
    _l_(4183)

    out.extend(_split_blueprint_path(name.rpartition(".")[0]))
    _l_(4182)
aux = out
_l_(4184)

exit(aux)
