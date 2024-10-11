# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
for self.force_gpu in self._gpu_modes():
    actual = self._LinSpaceNumConstant(0., 1., 32)
    expected = np.linspace(0., 1., 32)
    self.assertArrayNear(expected, actual, 1e-5)
