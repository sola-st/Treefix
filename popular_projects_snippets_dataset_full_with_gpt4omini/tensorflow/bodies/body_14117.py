# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
values = [StructuredTensor.from_pyval(v) for v in values]
with self.assertRaisesRegex(error_type, error_regex):
    array_ops.concat(values, axis)
