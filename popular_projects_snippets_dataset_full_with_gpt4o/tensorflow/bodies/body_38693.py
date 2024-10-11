# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
for dtype in [np.float32]:
    self._testDtype(dtype, use_gpu=True)
