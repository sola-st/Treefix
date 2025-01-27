# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
np.random.seed(100)
for _ in range(20):
    rank = np.random.randint(5, 15)
    shape = [np.random.randint(1, 4) for _ in range(rank)]
    arr = self.random_array(shape, dtype)
    sort_axis = np.random.choice(rank)
    with self.cached_session():
        self._test_sort(arr, sort_axis, 'ASCENDING')
