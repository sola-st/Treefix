# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
np.random.seed(7)
for shape in (0, 0), (2, 0), (0, 2), (4, 3, 0), (4, 0, 3), (0, 4, 3):
    self._testAll(np.random.randn(*shape), np.random.randn(shape[-1]))
