from typing import Callable, List # pragma: no cover

def call_with_mapped_captures(func: Callable, args: List): return func(*args) # pragma: no cover
def concrete(arg1: str, arg2: int): return f'Concrete: {arg1}, {arg2}' # pragma: no cover
merged_prefix = ['prefix1', 'prefix2'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
from l3.Runtime import _l_
aux = call_with_mapped_captures(concrete, [merged_prefix])
_l_(9585)
exit(aux)
