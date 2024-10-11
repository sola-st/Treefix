# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
if context.executing_eagerly():
    exit()

a = RaggedTensor.from_row_splits(
    array_ops.placeholder(dtypes.int32, shape=[None], name='a.values'),
    array_ops.placeholder(dtypes.int64, name='a.row_splits'),
    validate=False)
ragged_math_ops.reduce_sum(a)
self.assertLen(a.consumers(), 1)
