# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
original = StructuredTensor.from_pyval(
    {"x0": 2, "y": {"z": [[3, 5], [4]]}})  # pyformat: disable

with self.assertRaisesRegex(ValueError, "scalar"):
    random_ops.random_shuffle(original)
