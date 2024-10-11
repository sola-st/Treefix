type_spec = type('Mock', (object,), {'_from_tensor_list': lambda self, x: x})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
from l3.Runtime import _l_
aux = type_spec._from_tensor_list(encoded_value)  # pylint: disable=protected-access
_l_(22173)  # pylint: disable=protected-access
exit(aux)  # pylint: disable=protected-access
