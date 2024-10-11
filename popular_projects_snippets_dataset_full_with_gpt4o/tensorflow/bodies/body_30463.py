# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/denormal_test.py
"""Non-tf numpy code should treat denormals correctly."""
for dtype in np.float32, np.float64:
    tiny = np.finfo(dtype).tiny
    self.assertEqual(tiny, tiny / 16 * 16)
