# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_nd_op_test.py
if context.executing_eagerly():
    exit()
params = ragged_factory_ops.constant([['a', 'b'], ['c', 'd']])
indices1 = array_ops.placeholder(dtypes.int32, shape=None)
indices2 = array_ops.placeholder(dtypes.int32, shape=[None])

with self.assertRaisesRegex(ValueError,
                            'indices.rank be statically known.'):
    ragged_gather_ops.gather_nd(params, indices1)
with self.assertRaisesRegex(
    ValueError, r'indices.shape\[-1\] must be statically known.'):
    ragged_gather_ops.gather_nd(params, indices2)
