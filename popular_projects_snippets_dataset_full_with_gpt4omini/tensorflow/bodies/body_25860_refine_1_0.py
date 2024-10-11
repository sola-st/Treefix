to_ragged_spec = lambda spec: spec # pragma: no cover

class MockTensorSpec:  # Mock class for TensorSpec # pragma: no cover
    def __init__(self, tensor): # pragma: no cover
        self.shape = tensor.shape # pragma: no cover
        self.rank = tensor.shape.rank # pragma: no cover
    @classmethod # pragma: no cover
    def from_tensor(cls, tensor): # pragma: no cover
        return cls(tensor) # pragma: no cover
 # pragma: no cover
class MockRaggedTensor:  # Mock class for RaggedTensor # pragma: no cover
    @staticmethod # pragma: no cover
    def from_tensor(tensor, ragged_rank): # pragma: no cover
        return tensor # pragma: no cover
 # pragma: no cover
class MockRaggedSpec:  # Mock class for RaggedSpec # pragma: no cover
    def __init__(self, ragged_rank): # pragma: no cover
        self._ragged_rank = ragged_rank # pragma: no cover
    def _to_tensor_list(self, value): # pragma: no cover
        return [value] # pragma: no cover
to_ragged_spec = lambda spec: MockRaggedSpec(ragged_rank=1) # pragma: no cover
tensor_spec = MockTensorSpec # pragma: no cover
ragged_tensor = MockRaggedTensor # pragma: no cover

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
