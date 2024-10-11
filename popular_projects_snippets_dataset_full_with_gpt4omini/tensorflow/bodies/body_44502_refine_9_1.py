array_ops = type('Mock', (object,), {'shape': staticmethod(lambda x: tf.shape(x)), 'rank': staticmethod(lambda x: tf.rank(x))})() # pragma: no cover
control_flow_ops = type('Mock', (object,), {'Assert': staticmethod(lambda condition, data: None), 'cond': staticmethod(lambda pred, true_fn, false_fn: true_fn() if pred else false_fn())})() # pragma: no cover

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
