encoded_value = [1.0, 2.0, 3.0] # pragma: no cover

class MockTypeSpec:  # Simulating the type_spec with a mock class# pragma: no cover
    @staticmethod# pragma: no cover
    def _from_tensor_list(tensors):# pragma: no cover
        return tf.stack(tensors)# pragma: no cover
# pragma: no cover
type_spec = MockTypeSpec() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
from l3.Runtime import _l_
aux = type_spec._from_tensor_list(encoded_value)  # pylint: disable=protected-access
_l_(9873)  # pylint: disable=protected-access
exit(aux)  # pylint: disable=protected-access
