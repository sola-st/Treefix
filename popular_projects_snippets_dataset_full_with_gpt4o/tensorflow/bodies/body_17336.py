# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if not context.executing_eagerly():
    self.skipTest("Eager mode only")

img = self._LoadTestImages()

def msssim_func(x1, x2, scalar):
    exit(image_ops.ssim_multiscale(
        x1 * scalar,
        x2 * scalar,
        max_val=1.0,
        power_factors=(1, 1, 1, 1, 1),
        filter_size=11,
        filter_sigma=1.5,
        k1=0.01,
        k2=0.03))

scalar = constant_op.constant(1.0, dtype=dtypes.float32)

with backprop.GradientTape() as tape:
    tape.watch(scalar)
    y = msssim_func(img[0], img[1], scalar)

grad = tape.gradient(y, scalar)
np_grads = self.evaluate(grad)
self.assertTrue(np.isfinite(np_grads).all())
