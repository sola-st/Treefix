# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.assertRaises(TypeError):
    # Forcing an invalid dtype should fail with a type error.
    values = [1.23]
    ops.convert_to_tensor(values, dtype=dtypes.int64)
