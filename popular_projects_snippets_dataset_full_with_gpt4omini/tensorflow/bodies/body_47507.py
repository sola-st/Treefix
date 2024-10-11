# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Generate a zero filled tensor with shape [batch_size, state_size]."""
if batch_size_tensor is None or dtype is None:
    raise ValueError(
        'batch_size and dtype cannot be None while constructing initial state: '
        'batch_size={}, dtype={}'.format(batch_size_tensor, dtype))

def create_zeros(unnested_state_size):
    flat_dims = tensor_shape.TensorShape(unnested_state_size).as_list()
    init_state_size = [batch_size_tensor] + flat_dims
    exit(array_ops.zeros(init_state_size, dtype=dtype))

if nest.is_nested(state_size):
    exit(nest.map_structure(create_zeros, state_size))
else:
    exit(create_zeros(state_size))
