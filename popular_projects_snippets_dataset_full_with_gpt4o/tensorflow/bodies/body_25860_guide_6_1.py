 # pragma: no cover
 # pragma: no cover
def to_ragged_spec(spec): # pragma: no cover
    class MockSpec: # pragma: no cover
        def __init__(self): # pragma: no cover
            self._ragged_rank = 1 # pragma: no cover
        def _to_tensor_list(self, value): # pragma: no cover
            return [value] # pragma: no cover
    return MockSpec() # pragma: no cover
 # pragma: no cover
    print(f'Exited with value: {aux}') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/ragged_batch_op.py
from l3.Runtime import _l_
"""Re-encode Tensors as RaggedTensors."""
if (not isinstance(value, ops.Tensor) or
    value.shape.rank is None or
    value.shape.is_fully_defined()):
    _l_(21552)

    aux = value
    _l_(21547)
    exit(aux)
else:
    spec = to_ragged_spec(tensor_spec.TensorSpec.from_tensor(value))
    _l_(21548)
    if spec._ragged_rank > 0:
        _l_(21550)

        value = ragged_tensor.RaggedTensor.from_tensor(
            value, ragged_rank=spec._ragged_rank)  # pylint: disable=protected-access
        _l_(21549)  # pylint: disable=protected-access
    aux = spec._to_tensor_list(value)[0]  # pylint: disable=protected-access
    _l_(21551)  # pylint: disable=protected-access
    exit(aux)  # pylint: disable=protected-access
