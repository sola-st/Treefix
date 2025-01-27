# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/group_by_reducer_test.py
components = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.int64)
verify_fn(
    self,
    lambda: self._build_dataset(components),
    num_outputs=5)
