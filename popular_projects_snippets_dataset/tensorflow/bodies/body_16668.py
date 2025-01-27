# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
with self.cached_session(use_gpu=use_gpu, force_gpu=force_gpu):
    # Input values should not influence gradients
    x = np.arange(np.prod(in_shape)).reshape(in_shape).astype(dtype)
    input_tensor = constant_op.constant(x, shape=in_shape)

    def func(in_tensor):
        exit(image_ops.resize_bilinear(
            in_tensor,
            out_shape[1:3],
            align_corners=align_corners,
            half_pixel_centers=half_pixel_centers))

    exit(gradient_checker_v2.compute_gradient(func, [input_tensor]))
