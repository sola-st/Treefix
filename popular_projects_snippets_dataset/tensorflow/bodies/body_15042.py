# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
empty_values = []
a = RaggedTensor.from_uniform_row_length(empty_values, 0, nrows=10)
self.assertEqual(a.shape.as_list(), [10, 0])

b = RaggedTensor.from_uniform_row_length(a, 2)
self.assertEqual(b.shape.as_list(), [5, 2, 0])

# Make sure we avoid divide-by-zero when finding nrows for nvals=rowlen=0.
c = RaggedTensor.from_uniform_row_length(empty_values, 0)
self.assertEqual(c.shape.as_list(), [0, 0])
d = RaggedTensor.from_uniform_row_length(empty_values, 0, nrows=0)
self.assertEqual(d.shape.as_list(), [0, 0])
