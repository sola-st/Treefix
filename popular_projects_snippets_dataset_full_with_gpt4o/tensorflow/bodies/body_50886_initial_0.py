inner_concrete = type('Mock', (object,), {'_call_flat': lambda self, args, inputs: args[0]+sum(inputs), 'captured_inputs': [1, 2, 3]})() # pragma: no cover
args = [4] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_serialization.py
from l3.Runtime import _l_
aux = inner_concrete._call_flat(args, inner_concrete.captured_inputs)  # pylint:disable=protected-access
_l_(16391)  # pylint:disable=protected-access
exit(aux)  # pylint:disable=protected-access
