# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with self.cached_session():
    error_message = ("Empty tensors are not supported, but received shape "
                     r"\'\(0,\)\' at index 1")
    with self.assertRaisesRegex(ValueError, error_message):
        data_flow_ops.Barrier(
            (dtypes.float32, dtypes.float32), shapes=((1,), (0,)), name="B")
