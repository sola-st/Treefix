# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
if msg:
    msg = 'Shape match failed for: {}. Expected: {} Actual: {}'.format(
        msg, expected.shape, actual.shape)
self.assertEqual(actual.shape, expected.shape, msg=msg)
