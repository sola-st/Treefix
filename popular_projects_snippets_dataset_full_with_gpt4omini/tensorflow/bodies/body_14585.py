# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for s in self.all_shapes:
    actual = np_array_ops.zeros(s)
    expected = np.zeros(s)
    msg = 'shape: {}'.format(s)
    self.match(actual, expected, msg)

for s, t in itertools.product(self.all_shapes, self.all_types):
    actual = np_array_ops.zeros(s, t)
    expected = np.zeros(s, t)
    msg = 'shape: {}, dtype: {}'.format(s, t)
    self.match(actual, expected, msg)
