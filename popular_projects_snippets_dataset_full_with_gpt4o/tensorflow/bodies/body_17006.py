# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
fused = False
if not fused:
    # The tests are known to pass with the fused adjust_hue. We will enable
    # them when the fused implementation is the default.
    exit()
x_np = np.random.rand(2, 3) * 255.
delta_h = np.random.rand() * 2.0 - 1.0
fused = False
with self.assertRaisesRegex(ValueError, "Shape must be at least rank 3"):
    self._adjustHueTf(x_np, delta_h)
x_np = np.random.rand(4, 2, 4) * 255.
delta_h = np.random.rand() * 2.0 - 1.0
with self.assertRaisesOpError("input must have 3 channels"):
    self._adjustHueTf(x_np, delta_h)
