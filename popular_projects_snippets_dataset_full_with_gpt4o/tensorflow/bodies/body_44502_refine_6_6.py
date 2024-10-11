import numpy as np # pragma: no cover

s = type('Mock', (object,), {'shape': type('MockShape', (object,), {'ndims': True, 'dims': [type('MockDim', (object,), {'value': 3})]})()})() # pragma: no cover
array_ops = type('Mock', (object,), {'shape': lambda x: np.array([3]), 'rank': lambda x: np.array(2)})() # pragma: no cover
control_flow_ops = type('Mock', (object,), {'Assert': lambda cond, data: cond, 'cond': lambda pred, true_fn, false_fn: true_fn() if pred else false_fn()})() # pragma: no cover
gen_string_ops = type('Mock', (object,), {'string_join': lambda strings: ''.join(strings), 'as_string': lambda x: str(x)})() # pragma: no cover
ops = type('Mock', (object,), {'control_dependencies': lambda x: x})() # pragma: no cover
constant_op = type('Mock', (object,), {'constant': lambda value, dtype: value})() # pragma: no cover
dtypes = type('Mock', (object,), {'int32': 'int32'})() # pragma: no cover

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
