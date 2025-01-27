# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with ops.Graph().as_default():
    boxes_np = [[0, 0, 1, 1], [0, 0.2, 1, 1.2], [0, 0.4, 1, 1.4],
                [0, 0.6, 1, 1.6], [0, 0.8, 1, 1.8], [0, 2, 1, 2]]
    scores_np = [0.9, 0.75, 0.6, 0.5, 0.4, 0.3]
    max_output_size_np = 3
    iou_threshold_np = 0.5
    score_threshold_np = 0.1
    boxes = constant_op.constant(boxes_np)
    scores = constant_op.constant(scores_np)
    max_output_size = constant_op.constant(max_output_size_np)
    iou_threshold = constant_op.constant(iou_threshold_np)
    score_threshold = constant_op.constant(score_threshold_np)
    selected_indices, num_valid = image_ops.non_max_suppression_padded(
        boxes,
        scores,
        max_output_size,
        iou_threshold,
        score_threshold)
    # The output shape of the padded operation must be fully defined.
    self.assertEqual(selected_indices.shape.is_fully_defined(), False)
    with self.cached_session():
        self.assertAllClose(selected_indices, [0, 2, 4])
        self.assertEqual(num_valid.eval(), 3)
