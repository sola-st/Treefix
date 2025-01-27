# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
components = np.array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 0, 0, 2, 2, 0, 0],
                      dtype=np.int64)
self.verify_unused_iterator(
    lambda: self._build_dataset(components),
    num_outputs=12,
    verify_exhausted=False)
self.verify_multiple_breaks(
    lambda: self._build_dataset(components),
    num_outputs=12,
    verify_exhausted=False)
self.verify_reset_restored_iterator(
    lambda: self._build_dataset(components),
    num_outputs=12,
    verify_exhausted=False)
