# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_d9m_test.py
with test_util.force_cpu():
    for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
        params = self._genParams(dtype)
        image, boxes, box_indices, crop_size, injected_gradients = params

        with backprop.GradientTape(persistent=True) as tape:
            tape.watch([image, boxes])
            output = image_ops.crop_and_resize_v2(
                image, boxes, box_indices, crop_size, method='bilinear')
            upstream = output * injected_gradients

        image_gradients_a, boxes_gradients_a = tape.gradient(
            upstream, [image, boxes])
        for _ in range(5):
            image_gradients_b, boxes_gradients_b = tape.gradient(
                upstream, [image, boxes])
            if test_image_not_boxes:
                self.assertAllEqual(image_gradients_a, image_gradients_b)
            else:
                self.assertAllEqual(boxes_gradients_a, boxes_gradients_b)
