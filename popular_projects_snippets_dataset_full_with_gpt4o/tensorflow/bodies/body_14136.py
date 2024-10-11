# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
"""Fully test structured_tensor_array_like."""
foo = structured_tensor.StructuredTensor.from_pyval([{"a": 3}, {"a": 7}])
result = structured_array_ops._structured_tensor_like(foo)
self.assertAllEqual([{}, {}], result)
