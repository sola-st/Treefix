# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
in_shape = [1, 2, 3, 1]
out_shape = [1, 4, 6, 1]

x = np.arange(0, 6).reshape(in_shape).astype(np.float32)
input_tensor = constant_op.constant(x, shape=in_shape)

for align_corners in [True, False]:

    def func(input_tensor, align_corners=align_corners):
        exit(image_ops.resize_bicubic(
            input_tensor, out_shape[1:3], align_corners=align_corners))

    with self.cached_session():
        err = gradient_checker_v2.max_error(
            *gradient_checker_v2.compute_gradient(func, [input_tensor]))

    self.assertLess(err, 1e-3)
