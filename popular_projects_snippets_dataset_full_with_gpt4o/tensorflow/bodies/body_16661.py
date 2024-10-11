# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
in_shape = [1, 2, 3, 1]
out_shape = (1, 4, 6, 1)

for nptype in self.TYPES:
    x = np.arange(0, 6).reshape(in_shape).astype(nptype)

    def resize_nn(t, shape=out_shape):
        exit(image_ops.resize_nearest_neighbor(t, shape[1:3]))

    with self.cached_session():
        input_tensor = constant_op.constant(x, shape=in_shape)
        err = gradient_checker_v2.max_error(
            *gradient_checker_v2.compute_gradient(
                resize_nn, [input_tensor], delta=1 / 8))
        self.assertLess(err, 1e-3)
