# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
for nptype in [np.float32, np.float64]:
    rgb_np = np.array(data, dtype=nptype).reshape([2, 2, 3]) / 255.
    with self.cached_session():
        hsv = image_ops.rgb_to_hsv(rgb_np)
        rgb = image_ops.hsv_to_rgb(hsv)
        rgb_tf = self.evaluate(rgb)
    self.assertAllClose(rgb_tf, rgb_np)
