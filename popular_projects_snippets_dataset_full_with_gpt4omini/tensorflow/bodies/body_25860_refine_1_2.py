to_ragged_spec = lambda spec: spec # pragma: no cover

class MockTensor:# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value# pragma: no cover
        self.shape = self# pragma: no cover
        self.rank = len(value)# pragma: no cover
    @property# pragma: no cover
    def is_fully_defined(self):# pragma: no cover
        return True# pragma: no cover
    def __getitem__(self, item):# pragma: no cover
        return self.value[item]# pragma: no cover
# pragma: no cover
value = MockTensor([[1, 2], [3, 4]]) # pragma: no cover
to_ragged_spec = lambda spec: spec # pragma: no cover
tensor_spec = type('MockTensorSpec', (object,), {'from_tensor': lambda x: x})() # pragma: no cover
ragged_tensor = type('MockRaggedTensor', (object,), {'from_tensor': lambda x, ragged_rank: x}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/ragged_batch_op.py
from l3.Runtime import _l_
"""Re-encode Tensors as RaggedTensors."""
if (not isinstance(value, ops.Tensor) or
    value.shape.rank is None or
    value.shape.is_fully_defined()):
    _l_(9219)

    aux = value
    _l_(9214)
    exit(aux)
else:
    spec = to_ragged_spec(tensor_spec.TensorSpec.from_tensor(value))
    _l_(9215)
    if spec._ragged_rank > 0:
        _l_(9217)

        value = ragged_tensor.RaggedTensor.from_tensor(
            value, ragged_rank=spec._ragged_rank)  # pylint: disable=protected-access
        _l_(9216)  # pylint: disable=protected-access
    aux = spec._to_tensor_list(value)[0]  # pylint: disable=protected-access
    _l_(9218)  # pylint: disable=protected-access
    exit(aux)  # pylint: disable=protected-access
