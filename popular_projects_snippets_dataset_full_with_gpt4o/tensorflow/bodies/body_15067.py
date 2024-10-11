# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
if context.executing_eagerly():
    exit()

# Placeholder inputs.
a = RaggedTensor.from_row_splits(
    array_ops.placeholder(dtypes.int32, shape=[None], name='a.values'),
    array_ops.placeholder(dtypes.int64, name='a.row_splits'))
b = RaggedTensor.from_row_splits(
    array_ops.placeholder(dtypes.int32, shape=[None], name='b.values'),
    array_ops.placeholder(dtypes.int64, name='b.row_splits'))
c = array_ops.placeholder(dtypes.int32, shape=[], name='c')

# Feed values for placeholder inputs.
a_val = ragged_factory_ops.constant_value([[1, 2, 3], [4]])
b_val = ragged_factory_ops.constant_value([[5, 4, 3], [2]])
c_val = 3

# Compute some values.
r1 = ragged_math_ops.reduce_sum(a * b, axis=1)
r2 = ragged_math_ops.reduce_sum(a + c, axis=1)

with self.test_session() as session:
    handle = session.partial_run_setup([r1, r2], [a, b, c])

    res1 = session.partial_run(handle, r1, feed_dict={a: a_val, b: b_val})
    self.assertAllEqual(res1, [22, 8])

    res2 = session.partial_run(handle, r2, feed_dict={c: c_val})
    self.assertAllEqual(res2, [15, 7])
