# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
if not align_corners and test_util.is_xla_enabled():
    # Align corners is deprecated in TF2.0, but align_corners==False is not
    # supported by XLA.
    self.skipTest('align_corners==False not currently supported by XLA')
with self.session(force_gpu=True):
    seed = (
        hash(align_corners) % 256 + hash(half_pixel_centers) % 256 +
        hash(data_type) % 256)
    np.random.seed(seed)
    input_shape = (1, 25, 12, 3)  # NHWC
    output_shape = (1, 200, 250, 3)
    input_image = self._randomDataOp(input_shape, data_type)
    repeat_count = 3
    if context.executing_eagerly():

        def resize_bilinear_gradients(local_seed):
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

        for i in range(repeat_count):
            local_seed = seed + i  # select different upstream gradients
            result_a = resize_bilinear_gradients(local_seed)
            result_b = resize_bilinear_gradients(local_seed)
            self.assertAllEqual(result_a, result_b)
    else:  # graph mode
        upstream_gradients = array_ops.placeholder(
            dtypes.float32, shape=output_shape, name='upstream_gradients')
        output_image = image_ops.resize_bilinear(
            input_image,
            output_shape[1:3],
            align_corners=align_corners,
            half_pixel_centers=half_pixel_centers)
        gradient_injector_output = output_image * upstream_gradients
        # The gradient function behaves as if grad_ys is multiplied by the op
        # gradient result, not passing the upstream gradients through the op's
        # gradient generation graph. This is the reason for using the
        # gradient injector
        resize_bilinear_gradients = gradients_impl.gradients(
            gradient_injector_output,
            input_image,
            grad_ys=None,
            colocate_gradients_with_ops=True)[0]
        for i in range(repeat_count):
            feed_dict = {upstream_gradients: self._randomNDArray(output_shape)}
            result_a = resize_bilinear_gradients.eval(feed_dict=feed_dict)
            result_b = resize_bilinear_gradients.eval(feed_dict=feed_dict)
            self.assertAllEqual(result_a, result_b)
