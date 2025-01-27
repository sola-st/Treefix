# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    image, boxes, box_indices, crop_size = self._genParams(dtype)
    with backprop.GradientTape(persistent=True) as tape:
        tape.watch(image)
        tape.watch(boxes)
        op_output = image_ops.crop_and_resize_v2(image, boxes, box_indices,
                                                 crop_size)
    image_error_message = ('Deterministic GPU implementation of' +
                           ' CropAndResizeBackpropImage not available')
    with self.assertRaisesRegex(errors_impl.UnimplementedError,
                                image_error_message):
        result = tape.gradient(op_output, image)
        self.evaluate(result)
    expected_error_message = ('Deterministic GPU implementation of' +
                              ' CropAndResizeBackpropBoxes not available')
    if context.executing_eagerly():
        # With eager execution, the backprop-to-image code is apparently
        # executed (first), even when its output is never used.
        expected_error_message = image_error_message
    with self.assertRaisesRegex(errors_impl.UnimplementedError,
                                expected_error_message):
        result = tape.gradient(op_output, boxes)
        self.evaluate(result)
