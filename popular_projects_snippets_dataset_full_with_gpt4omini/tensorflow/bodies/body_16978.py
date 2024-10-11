# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Test case for GitHub issue 54855.
data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
for dtype in [
    dtypes.float32, dtypes.float64, dtypes.float16, dtypes.bfloat16
]:
    with self.cached_session(use_gpu=False):
        rgb = math_ops.cast(
            np.array(data, np.float32).reshape([2, 2, 3]) / 255., dtype=dtype)
        hsv = image_ops.rgb_to_hsv(rgb)
        val = image_ops.hsv_to_rgb(hsv)
        out = self.evaluate(val)
        self.assertAllClose(rgb, out, atol=1e-2)
