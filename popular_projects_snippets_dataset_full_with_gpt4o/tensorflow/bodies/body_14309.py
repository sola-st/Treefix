# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_logic_test.py
msg_ = 'Expected: {} Actual: {}'.format(expected, actual)
if msg:
    msg = '{} {}'.format(msg_, msg)
else:
    msg = msg_
self.assertIsInstance(actual, np_arrays.ndarray)
self.match_dtype(actual, expected, msg)
self.match_shape(actual, expected, msg)
if not actual.shape.rank:
    self.assertEqual(actual.tolist(), expected.tolist())
else:
    self.assertSequenceEqual(actual.tolist(), expected.tolist())
