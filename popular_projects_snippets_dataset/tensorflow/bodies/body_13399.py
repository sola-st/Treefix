# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops_test.py
if context.executing_eagerly():
    self.skipTest('sparse_spaceholder is only available in graph context.')
input_a = array_ops.sparse_placeholder(dtypes.float32, shape=(2, 1))
input_b = array_ops.sparse_placeholder(dtypes.float32, shape=(2, 2))

result = sparse_ops.sparse_concat_v2(axis=1, sp_inputs=[input_a, input_b])
self.assertEqual(result.shape, [2, 3])
