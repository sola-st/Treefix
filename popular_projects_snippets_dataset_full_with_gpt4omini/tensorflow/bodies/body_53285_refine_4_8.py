from typing import List # pragma: no cover

class MockTypeSpec(object): # pragma: no cover
    pass
type_spec = MockTypeSpec() # pragma: no cover

class MockTypeSpec(object): # pragma: no cover
    def _from_tensor_list(self, tensor_list): # pragma: no cover
        return tensor_list # pragma: no cover
type_spec = MockTypeSpec() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
from l3.Runtime import _l_
aux = type_spec._from_tensor_list(encoded_value)  # pylint: disable=protected-access
_l_(9873)  # pylint: disable=protected-access
exit(aux)  # pylint: disable=protected-access
