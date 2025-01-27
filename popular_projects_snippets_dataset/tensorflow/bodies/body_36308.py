# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
nums = np.array([1, 2, 3, 4, 5, 6])
with self.assertRaisesRegex(
    TypeError, r"two structures don't have the same nested structure"):
    # lambda emits tuple, but dtype is a list
    map_fn.map_fn(
        lambda x: ((x + 3) * 2, -(x + 3) * 2),
        nums,
        dtype=[dtypes.int64, dtypes.int64])
