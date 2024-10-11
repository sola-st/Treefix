from typing import Any # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._element_spec = 'element_spec_value' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/group_by_window_op.py
from l3.Runtime import _l_
aux = self._element_spec
_l_(5484)
exit(aux)
