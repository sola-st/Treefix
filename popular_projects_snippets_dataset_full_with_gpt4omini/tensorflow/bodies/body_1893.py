# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
"""Tests the RGB to HSV conversion matches a reference implementation."""
for nptype in self.float_types:
    rgb_flat = _generate_numpy_random_rgb((64, 3)).astype(nptype)
    rgb_np = rgb_flat.reshape(4, 4, 4, 3)  # pylint: disable=too-many-function-args
    hsv_np = np.array([
        colorsys.rgb_to_hsv(
            r.astype(np.float64), g.astype(np.float64), b.astype(np.float64))
        for r, g, b in rgb_flat
    ])
    hsv_np = hsv_np.reshape(4, 4, 4, 3)  # pylint: disable=too-many-function-args
    with self.session():
        placeholder = array_ops.placeholder(nptype)
        with self.test_scope():
            hsv_op = image_ops.rgb_to_hsv(placeholder)
        hsv_tf = hsv_op.eval(feed_dict={placeholder: rgb_np})
    self.assertAllCloseAccordingToType(hsv_tf, hsv_np)
