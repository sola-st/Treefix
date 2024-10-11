# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for s in self.all_shapes:
    actual = np_array_ops.empty(s)
    expected = np.empty(s)
    msg = 'shape: {}'.format(s)
    self.match_shape(actual, expected, msg)
    self.match_dtype(actual, expected, msg)

for s, t in itertools.product(self.all_shapes, self.all_types):
    actual = np_array_ops.empty(s, t)
    expected = np.empty(s, t)
    msg = 'shape: {}, dtype: {}'.format(s, t)
    self.match_shape(actual, expected, msg)
    self.match_dtype(actual, expected, msg)
