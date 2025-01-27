# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
st = StructuredTensor.from_pyval(st)
result = array_ops.expand_dims(st, axis)
self.assertAllEqual(result, expected)
