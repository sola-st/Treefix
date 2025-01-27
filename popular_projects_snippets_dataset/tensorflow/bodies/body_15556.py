# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_batch_gather_op_test.py
if context.executing_eagerly():
    exit()
params = [['a', 'b'], ['c', 'd']]
indices = array_ops.placeholder(dtypes.int32, shape=None)
ragged_indices = ragged_tensor.RaggedTensor.from_row_splits(
    indices, [0, 2, 4])

with self.assertRaisesRegex(
    ValueError, r'batch_dims=-1 may only be negative '
    r'if rank\(indices\) is statically known.'):
    ragged_batch_gather_ops.batch_gather(params, indices)

with self.assertRaisesRegex(
    ValueError, r'batch_dims=-1 may only be negative '
    r'if rank\(indices\) is statically known.'):
    ragged_batch_gather_ops.batch_gather(params, ragged_indices)
