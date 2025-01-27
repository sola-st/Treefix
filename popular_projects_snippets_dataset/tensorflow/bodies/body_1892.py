# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
data = [0, 5, 13, 54, 135, 226, 37, 8, 234, 90, 255, 1]
for nptype in self.float_types:
    rgb_np = np.array(data, dtype=nptype).reshape([2, 2, 3]) / 255.
    with self.session():
        placeholder = array_ops.placeholder(nptype)
        with self.test_scope():
            hsv = image_ops.rgb_to_hsv(placeholder)
            rgb = image_ops.hsv_to_rgb(hsv)
        rgb_tf = rgb.eval(feed_dict={placeholder: rgb_np})
    self.assertAllCloseAccordingToType(rgb_tf, rgb_np, bfloat16_atol=0.03)
