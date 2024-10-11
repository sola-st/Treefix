def call_with_mapped_captures(concrete, merged_prefix): return concrete + merged_prefix # pragma: no cover

concrete = 'Hello, ' # pragma: no cover
merged_prefix = 'world!' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
from l3.Runtime import _l_
aux = call_with_mapped_captures(concrete, [merged_prefix])
_l_(9585)
exit(aux)
