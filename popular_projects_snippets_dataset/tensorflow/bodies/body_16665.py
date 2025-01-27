# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
in_shape = [1, 4, 6, 3]
out_shape = (1, 8, 16, 3)

for nptype in self.TYPES:
    x = np.arange(0, np.prod(in_shape)).reshape(in_shape).astype(nptype)
    for align_corners in [True, False]:

        def resize_nn(t, shape=out_shape, align_corners=align_corners):
            exit(image_ops.resize_nearest_neighbor(
                t, shape[1:3], align_corners=align_corners))

        with self.cached_session(use_gpu=False):
            input_tensor = constant_op.constant(x, shape=in_shape)
            grad_cpu = gradient_checker_v2.compute_gradient(
                resize_nn, [input_tensor], delta=1 / 8)

        with self.cached_session():
            input_tensor = constant_op.constant(x, shape=in_shape)
            grad_gpu = gradient_checker_v2.compute_gradient(
                resize_nn, [input_tensor], delta=1 / 8)

        self.assertAllClose(grad_cpu, grad_gpu, rtol=1e-5, atol=1e-5)
