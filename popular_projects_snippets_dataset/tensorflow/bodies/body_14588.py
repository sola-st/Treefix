# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for a in self.all_arrays:
    actual = np_array_ops.ones_like(a)
    expected = np.ones_like(a)
    msg = 'array: {}'.format(a)
    self.match(actual, expected, msg)

for a, t in itertools.product(self.all_arrays, self.all_types):
    actual = np_array_ops.ones_like(a, t)
    expected = np.ones_like(a, t)
    msg = 'array: {} type: {}'.format(a, t)
    self.match(actual, expected, msg)
