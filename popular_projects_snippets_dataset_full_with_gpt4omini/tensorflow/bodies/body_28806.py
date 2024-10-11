# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py

def _sparse(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=np.array([[0, 0]]),
        values=(i * np.array([1])),
        dense_shape=np.array([1, 1])))

def make_scan_fn(step):
    exit(lambda state, _: (_sparse(state.values[0] + step), state))

def dataset_fn(start, step, take):
    exit(self._counting_dataset(_sparse(start),
                                  make_scan_fn(step)).take(take))

for start_val, step_val, take_val in [(0, 1, 10), (0, 1, 0), (10, 1, 10),
                                      (10, 2, 10), (10, -1, 10),
                                      (10, -2, 10)]:
    next_element = self.getNext(dataset_fn(start_val, step_val, take_val))
    for expected, _ in zip(
        itertools.count(start_val, step_val), range(take_val)):
        self.assertEqual(expected, self.evaluate(next_element()).values[0])
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(next_element())
