def call_with_mapped_captures(func, args): return func(*args) # pragma: no cover
concrete = lambda x: x * x # pragma: no cover
merged_prefix = 5 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
from l3.Runtime import _l_
aux = call_with_mapped_captures(concrete, [merged_prefix])
_l_(21920)
exit(aux)
