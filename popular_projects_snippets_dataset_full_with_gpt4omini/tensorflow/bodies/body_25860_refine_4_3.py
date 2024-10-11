def to_ragged_spec(spec): return spec # pragma: no cover

def to_ragged_spec(spec): return type('RaggedSpec', (), {'_ragged_rank': 1, '_to_tensor_list': lambda self, x: [x]})() # pragma: no cover
class tensor_spec: # pragma: no cover
    class TensorSpec: # pragma: no cover
        @staticmethod # pragma: no cover
        def from_tensor(tensor): return tensor # pragma: no cover
ragged_tensor = type('MockRaggedTensor', (), {'from_tensor': staticmethod(lambda x, ragged_rank: x)}) # pragma: no cover

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
