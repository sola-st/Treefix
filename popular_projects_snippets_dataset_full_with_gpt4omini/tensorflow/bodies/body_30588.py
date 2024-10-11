# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
for self.force_gpu in self._gpu_modes():
    # Test some cases that produce last values not equal to "stop" when
    # computed via start + (num - 1) * ((stop - start) / (num - 1)), since
    # float arithmetic will introduce error through precision loss.
    self.assertAllEqual(
        self._LinSpace(0., 1., 42)[[0, -1]], np.array([0., 1.], np.float32))
    self.assertAllEqual(
        self._LinSpace(-1., 0., 42)[[0, -1]], np.array([-1., 0.], np.float32))
    self.assertAllEqual(
        self._LinSpace(.1, .2, 4)[[0, -1]], np.array([.1, .2], np.float32))
    # Check a case for float64 error too.
    self.assertAllEqual(
        self._LinSpace(np.array(0., np.float64), .1, 12)[[0, -1]],
        np.array([0., .1], np.float64))
