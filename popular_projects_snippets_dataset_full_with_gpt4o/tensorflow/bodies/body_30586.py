# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
for self.force_gpu in self._gpu_modes():
    self.assertArrayNear(self._LinSpace(-1., 5., 1), np.array([-1.]), 1e-5)
    self.assertArrayNear(
        self._LinSpace(-1., 5., 2), np.array([-1., 5.]), 1e-5)
    self.assertArrayNear(
        self._LinSpace(-1., 5., 3), np.array([-1., 2., 5.]), 1e-5)
    self.assertArrayNear(
        self._LinSpace(-1., 5., 4), np.array([-1., 1., 3., 5.]), 1e-5)
