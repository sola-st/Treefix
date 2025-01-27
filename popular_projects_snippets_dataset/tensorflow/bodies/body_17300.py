# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if not context.executing_eagerly() and run_func_eagerly:
    # Skip running tf.function eagerly in V1 mode.
    self.skipTest("Skip test that runs tf.function eagerly in V1 mode.")
else:

    @def_function.function
    def func(boxes, scores, max_output_size, iou_threshold):
        boxes = constant_op.constant(boxes_np)
        scores = constant_op.constant(scores_np)
        max_output_size = constant_op.constant(max_output_size_np)
        iou_threshold = constant_op.constant(iou_threshold_np)

        yp, nvp = image_ops.non_max_suppression_padded(
            boxes,
            scores,
            max_output_size,
            iou_threshold,
            pad_to_max_output_size=True)

        y, n = image_ops.non_max_suppression_padded(
            boxes,
            scores,
            max_output_size,
            iou_threshold,
            pad_to_max_output_size=False)

        # The output shape of the padded operation must be fully defined.
        self.assertEqual(yp.shape.is_fully_defined(), True)
        self.assertEqual(y.shape.is_fully_defined(), False)

        exit((yp, nvp, y, n))

    boxes_np = [[0, 0, 1, 1], [0, 0.1, 1, 1.1], [0, -0.1, 1, 0.9],
                [0, 10, 1, 11], [0, 10.1, 1, 11.1], [0, 100, 1, 101]]
    scores_np = [0.9, 0.75, 0.6, 0.95, 0.5, 0.3]
    max_output_size_np = 5
    iou_threshold_np = 0.5

    selected_indices_padded, num_valid_padded, selected_indices, num_valid = \
          func(boxes_np, scores_np, max_output_size_np, iou_threshold_np)

    with self.cached_session():
        with test_util.run_functions_eagerly(run_func_eagerly):
            self.assertAllClose(selected_indices_padded, [3, 0, 5, 0, 0])
            self.assertEqual(self.evaluate(num_valid_padded), 3)
            self.assertAllClose(selected_indices, [3, 0, 5])
            self.assertEqual(self.evaluate(num_valid), 3)
