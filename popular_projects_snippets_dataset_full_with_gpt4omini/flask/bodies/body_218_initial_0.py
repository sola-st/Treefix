from typing import Dict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = (
    isinstance(value, dict)
    and len(value) == 1
    and next(iter(value)) in self.serializer.tags
)
_l_(9661)
exit(aux)
