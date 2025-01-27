# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
for self.force_gpu in self._gpu_modes():
    self.assertArrayNear(self._LinSpace(5., 5., 1), np.array([5.]), 1e-5)
    self.assertArrayNear(self._LinSpace(5., 5., 2), np.array([5.] * 2), 1e-5)
    self.assertArrayNear(self._LinSpace(5., 5., 3), np.array([5.] * 3), 1e-5)
    self.assertArrayNear(self._LinSpace(5., 5., 4), np.array([5.] * 4), 1e-5)
