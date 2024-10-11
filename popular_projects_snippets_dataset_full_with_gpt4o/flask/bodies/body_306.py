# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/helpers.py
from l3.Runtime import _l_
out: t.List[str] = [name]
_l_(22485)

if "." in name:
    _l_(22487)

    out.extend(_split_blueprint_path(name.rpartition(".")[0]))
    _l_(22486)
aux = out
_l_(22488)

exit(aux)
