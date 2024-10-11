# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
ph_values = array_ops.placeholder_with_default([1, 2, 3, 4, 5, 6], [None])
ph_rowlen = array_ops.placeholder_with_default(3, None)
rt1 = RaggedTensor.from_uniform_row_length(ph_values, 3)
rt2 = RaggedTensor.from_uniform_row_length(ph_values, ph_rowlen)
rt3 = RaggedTensor.from_uniform_row_length([1, 2, 3, 4, 5, 6], ph_rowlen)
self.assertAllEqual(rt1, [[1, 2, 3], [4, 5, 6]])
self.assertAllEqual(rt2, [[1, 2, 3], [4, 5, 6]])
self.assertAllEqual(rt3, [[1, 2, 3], [4, 5, 6]])
if context.executing_eagerly():
    self.assertEqual(rt1.shape.as_list(), [2, 3])
    self.assertEqual(rt2.shape.as_list(), [2, 3])
    self.assertEqual(rt3.shape.as_list(), [2, 3])
else:
    self.assertEqual(rt1.shape.as_list(), [None, 3])
    self.assertEqual(rt2.shape.as_list(), [None, None])
    self.assertEqual(rt3.shape.as_list(), [None, None])

b = RaggedTensor.from_uniform_row_length(rt1, 2)
self.assertAllEqual(b, [[[1, 2, 3], [4, 5, 6]]])

# Make sure we avoid divide-by-zero when finding nrows for nvals=rowlen=0.
ph_empty_values = array_ops.placeholder_with_default(
    array_ops.zeros([0], dtypes.int64), [None])
ph_zero = array_ops.placeholder_with_default(0, [])
c = RaggedTensor.from_uniform_row_length(ph_empty_values, ph_zero)
if context.executing_eagerly():
    self.assertEqual(c.shape.as_list(), [0, 0])
else:
    self.assertEqual(c.shape.as_list(), [None, None])
