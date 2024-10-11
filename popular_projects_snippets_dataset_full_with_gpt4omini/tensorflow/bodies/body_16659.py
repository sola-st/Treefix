# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
in_shape = [1, 2, 2, 1]
out_shape = [1, 4, 6, 1]

for nptype in self.TYPES:
    x = np.arange(0, 4).reshape(in_shape).astype(nptype)

    input_tensor = constant_op.constant(x, shape=in_shape)
    resize_out = image_ops.resize_nearest_neighbor(input_tensor,
                                                   out_shape[1:3])
    with self.cached_session():
        self.assertEqual(out_shape, list(resize_out.get_shape()))
        resize_out = self.evaluate(resize_out)
    self.assertEqual(out_shape, list(resize_out.shape))
