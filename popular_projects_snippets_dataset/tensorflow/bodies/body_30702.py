# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
expected_roll = np.roll(np_input, shift, axis)
with self.cached_session():
    roll = manip_ops.roll(np_input, shift, axis)
    self.assertAllEqual(roll, expected_roll)
