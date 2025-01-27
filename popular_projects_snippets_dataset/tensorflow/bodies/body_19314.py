# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
with self.session(), test_util.force_gpu():
    input_image = array_ops.zeros((1, 2, 2, 1), dtype=data_type)
    with backprop.GradientTape() as tape:
        tape.watch(input_image)
        output_image = image_ops.resize_nearest_neighbor(
            input_image, (3, 3),
            align_corners=align_corners,
            half_pixel_centers=half_pixel_centers)
    with self.assertRaisesRegex(
        errors.UnimplementedError,
        'A deterministic GPU implementation of ResizeNearestNeighborGrad' +
        ' is not currently available.'):
        gradient = tape.gradient(output_image, input_image)
        self.evaluate(gradient)
