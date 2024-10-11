to_ragged_spec = type('Mock', (object,), {'__call__': lambda self, x: type('RaggedSpec', (object,), {'_ragged_rank': 1, '_to_tensor_list': lambda self, x: [tf.constant([[1, 2], [3, 4]], dtype=tf.int32)]})()})() # pragma: no cover
tensor_spec = type('Mock', (object,), {'TensorSpec': type('MockTensorSpec', (object,), {'from_tensor': staticmethod(lambda x: type('TensorSpec', (object,), {})())})()})() # pragma: no cover
ragged_tensor = type('MockRaggedTensor', (object,), {'from_tensor': staticmethod(lambda x, ragged_rank: type('RaggedTensor', (object,), {})())})() # pragma: no cover

to_ragged_spec = lambda spec: spec # pragma: no cover
tensor_spec = type('Mock', (object,), {'TensorSpec': type('TensorSpec', (object,), {'from_tensor': staticmethod(lambda x: None)})})() # pragma: no cover
ragged_tensor = type('MockRaggedTensor', (object,), {'from_tensor': staticmethod(lambda x, ragged_rank: None), 'RaggedTensor': None})() # pragma: no cover

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
