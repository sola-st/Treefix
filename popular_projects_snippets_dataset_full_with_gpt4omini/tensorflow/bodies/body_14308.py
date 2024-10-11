# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_logic_test.py
if msg:
    msg = 'Dtype match failed for: {}. Expected: {} Actual: {}.'.format(
        msg, expected.dtype, actual.dtype)
self.assertEqual(actual.dtype, expected.dtype, msg=msg)
