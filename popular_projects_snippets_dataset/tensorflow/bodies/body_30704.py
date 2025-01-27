# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
self._testRoll(np_input, shift, axis)
if np_input.dtype == np.float32:
    self._testGradient(np_input, shift, axis)
