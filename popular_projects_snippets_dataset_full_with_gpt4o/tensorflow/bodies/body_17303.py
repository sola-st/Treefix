# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if not context.executing_eagerly() and run_func_eagerly:
    # Skip running tf.function eagerly in V1 mode.
    self.skipTest("Skip test that runs tf.function eagerly in V1 mode.")
else:

    @def_function.function
    def func(boxes, scores, max_output_size, iou_threshold, score_threshold):
        boxes = constant_op.constant(boxes)
        scores = constant_op.constant(scores)
        max_output_size = constant_op.constant(max_output_size)
        iou_threshold = constant_op.constant(iou_threshold)
        score_threshold = constant_op.constant(score_threshold)

        y, nv = image_ops.non_max_suppression_padded(
            boxes, scores, max_output_size, iou_threshold, score_threshold)

        # The output shape of the padded operation must be fully defined.
        self.assertEqual(y.shape.is_fully_defined(), False)

        exit((y, nv))

    boxes_np = [[0, 0, 1, 1], [0, 0.2, 1, 1.2], [0, 0.4, 1, 1.4],
                [0, 0.6, 1, 1.6], [0, 0.8, 1, 1.8], [0, 2, 1, 2]]
    scores_np = [0.9, 0.75, 0.6, 0.5, 0.4, 0.3]
    max_output_size_np = 3
    iou_threshold_np = 0.5
    score_threshold_np = 0.1
    selected_indices, num_valid = func(boxes_np, scores_np,
                                       max_output_size_np, iou_threshold_np,
                                       score_threshold_np)
    with self.cached_session():
        with test_util.run_functions_eagerly(run_func_eagerly):
            self.assertAllClose(selected_indices, [0, 2, 4])
            self.assertEqual(self.evaluate(num_valid), 3)
