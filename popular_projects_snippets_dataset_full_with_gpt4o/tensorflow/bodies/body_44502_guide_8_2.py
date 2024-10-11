import sys # pragma: no cover

class MockDim: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
class MockShape: # pragma: no cover
    def __init__(self, ndims, dims): # pragma: no cover
        self.ndims = ndims # pragma: no cover
        self.dims = [MockDim(dim) for dim in dims] # pragma: no cover
mock_shape = MockShape(2, [None, 3]) # pragma: no cover
s = type('MockTensor', (object,), {'shape': mock_shape})() # pragma: no cover
exit = sys.exit # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
from l3.Runtime import _l_
"""Overload of len_ for Tensor arguments."""
# Statically shaped tensors: length is known ahead of time.
if s.shape.ndims and s.shape.dims[0].value is not None:
    _l_(18284)

    aux = s.shape.dims[0].value
    _l_(18283)
    exit(aux)

# Static shape of unknown dimensions: use dynamic shape but statically
# check that it's a scalar.
shape = array_ops.shape(s)
_l_(18285)

assert shape.shape, 'shape tensor of zero size? {}'.format(shape)
_l_(18286)

if shape.shape[0] == 0:
    _l_(18288)

    raise ValueError(
        'len requires a non-scalar tensor, got one of shape {}'.format(shape))
    _l_(18287)

if shape.shape.dims[0].value is not None:
    _l_(18290)

    aux = array_ops.shape(s)[0]
    _l_(18289)
    exit(aux)

# Fully dynamic shape: use ops.
rank = array_ops.rank(s)
_l_(18291)

def raise_zero_rank_error():
    _l_(18295)

    msg = gen_string_ops.string_join(
        ['len requires non-zero rank, got ',
         gen_string_ops.as_string(rank)])
    _l_(18292)
    with ops.control_dependencies([control_flow_ops.Assert(False, [msg])]):
        _l_(18294)

        aux = constant_op.constant(0, dtype=dtypes.int32)
        _l_(18293)
        exit(aux)
aux = control_flow_ops.cond(rank > 0, lambda: array_ops.shape(s)[0],
                             raise_zero_rank_error)
_l_(18296)

exit(aux)
