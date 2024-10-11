# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
"""Fully test structured_tensor_array_like."""
foo = array_ops.zeros(shape=[])
result = structured_array_ops._structured_tensor_like(foo)
self.assertAllEqual({}, result)
