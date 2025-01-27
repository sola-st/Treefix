# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
"""There was a bug in a case in a private function.

    This was difficult to reach externally, so I wrote a test
    to check it directly.
    """
rt = ragged_tensor.RaggedTensor.from_row_splits(
    array_ops.zeros(shape=[5, 3]), [0, 3, 5])
result = structured_array_ops._structured_tensor_like(rt)
self.assertEqual(3, result.rank)
