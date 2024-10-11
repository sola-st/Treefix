# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
in_shape = [2, 20, 30, 3]
out_shape = [2, 20, 30, 3]

for nptype in self.TYPES:
    x = np.random.randint(0, high=255, size=[2, 20, 30, 3]).astype(nptype)
    rgb_input_tensor = constant_op.constant(x, shape=in_shape)
    hsv_out = gen_image_ops.rgb_to_hsv(rgb_input_tensor)
    with self.cached_session():
        self.assertEqual(out_shape, list(hsv_out.get_shape()))
    hsv_out = self.evaluate(hsv_out)
    self.assertEqual(out_shape, list(hsv_out.shape))
