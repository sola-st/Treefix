# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
with self.assertRaisesRegex(ValueError, "values must not be an empty list"):
    structured_array_ops.concat([], 0)
