# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
np.random.seed(42)
for _ in range(20):
    rank = np.random.randint(1, 3)
    shape = [np.random.randint(0, 20) for _ in range(rank)]
    arr = self.random_array(shape, dtype)
    sort_axis = np.random.choice(rank)
    if negative_axis:
        sort_axis = -1 - sort_axis
    with self.cached_session():
        self._test_sort(arr, sort_axis, direction)
