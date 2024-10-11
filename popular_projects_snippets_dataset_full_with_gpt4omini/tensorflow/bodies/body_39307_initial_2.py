from typing import List # pragma: no cover

def call_with_mapped_captures(fn: callable, args: List) -> None: pass # pragma: no cover
concrete = lambda x: x * 2 # pragma: no cover
merged_prefix = 'prefix_' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
from l3.Runtime import _l_
aux = call_with_mapped_captures(concrete, [merged_prefix])
_l_(9585)
exit(aux)
