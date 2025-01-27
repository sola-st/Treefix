# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
np.random.seed(local_seed)
upstream_gradients = self._randomDataOp(output_shape, dtypes.float32)
with backprop.GradientTape(persistent=True) as tape:
    tape.watch(input_image)
    output_image = image_ops.resize_bilinear(
        input_image,
        output_shape[1:3],
        align_corners=align_corners,
        half_pixel_centers=half_pixel_centers)
    gradient_injector_output = output_image * upstream_gradients
exit(tape.gradient(gradient_injector_output, input_image))
