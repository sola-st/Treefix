# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
values = [StructuredTensor.from_pyval(v) for v in values]
actual = array_ops.concat(values, axis)
self.assertAllEqual(actual, expected)
