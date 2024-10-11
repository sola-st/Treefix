class MockTensor:  # Create a mock class to simulate the tensor behavior. # pragma: no cover
    def __init__(self, data): # pragma: no cover
        self.data = data # pragma: no cover
    @property # pragma: no cover
    def ndim(self): # pragma: no cover
        return len(self.shape) # pragma: no cover
    @property # pragma: no cover
    def dims(self): # pragma: no cover
        return [MockDim(dim) for dim in self.shape] # pragma: no cover
class MockDim:  # Mock class to simulate dimension behavior. # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
s = MockTensor([[1, 2, 3], [4, 5, 6]]) # pragma: no cover
array_ops = type('Mock', (object,), {'shape': lambda x: tf.shape(s.data), 'rank': lambda x: tf.rank(s.data)})() # pragma: no cover
control_flow_ops = type('Mock', (object,), {'Assert': lambda condition, data: None, 'cond': lambda pred, true_fn, false_fn: true_fn() if pred else false_fn()})() # pragma: no cover
gen_string_ops = type('Mock', (object,), {'string_join': lambda inputs: ' '.join(inputs), 'as_string': lambda x: str(x)})() # pragma: no cover
constant_op = type('Mock', (object,), {'constant': lambda value, dtype: tf.constant(value, dtype=dtype)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
from l3.Runtime import _l_
"""Overload of len_ for Tensor arguments."""
# Statically shaped tensors: length is known ahead of time.
if s.shape.ndims and s.shape.dims[0].value is not None:
    _l_(6144)

    aux = s.shape.dims[0].value
    _l_(6143)
    exit(aux)

# Static shape of unknown dimensions: use dynamic shape but statically
# check that it's a scalar.
shape = array_ops.shape(s)
_l_(6145)

assert shape.shape, 'shape tensor of zero size? {}'.format(shape)
_l_(6146)

if shape.shape[0] == 0:
    _l_(6148)

    raise ValueError(
        'len requires a non-scalar tensor, got one of shape {}'.format(shape))
    _l_(6147)

if shape.shape.dims[0].value is not None:
    _l_(6150)

    aux = array_ops.shape(s)[0]
    _l_(6149)
    exit(aux)

# Fully dynamic shape: use ops.
rank = array_ops.rank(s)
_l_(6151)

def raise_zero_rank_error():
    _l_(6155)

    msg = gen_string_ops.string_join(
        ['len requires non-zero rank, got ',
         gen_string_ops.as_string(rank)])
    _l_(6152)
    with ops.control_dependencies([control_flow_ops.Assert(False, [msg])]):
        _l_(6154)

        aux = constant_op.constant(0, dtype=dtypes.int32)
        _l_(6153)
        exit(aux)
aux = control_flow_ops.cond(rank > 0, lambda: array_ops.shape(s)[0],
                             raise_zero_rank_error)
_l_(6156)

exit(aux)
