# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with ops.Graph().as_default():
    boxes_np = [[0, 0, 1, 1], [0, 0.1, 1, 1.1], [0, -0.1, 1, 0.9],
                [0, 10, 1, 11], [0, 10.1, 1, 11.1], [0, 100, 1, 101]]
    scores_np = [0.9, 0.75, 0.6, 0.95, 0.5, 0.3]
    max_output_size_np = 5
    iou_threshold_np = 0.5
    boxes = constant_op.constant(boxes_np)
    scores = constant_op.constant(scores_np)
    max_output_size = constant_op.constant(max_output_size_np)
    iou_threshold = constant_op.constant(iou_threshold_np)
    selected_indices_padded, num_valid_padded = \
          image_ops.non_max_suppression_padded(
            boxes,
            scores,
            max_output_size,
            iou_threshold,
            pad_to_max_output_size=True)
    selected_indices, num_valid = image_ops.non_max_suppression_padded(
        boxes,
        scores,
        max_output_size,
        iou_threshold,
        pad_to_max_output_size=False)
    # The output shape of the padded operation must be fully defined.
    self.assertEqual(selected_indices_padded.shape.is_fully_defined(), True)
    self.assertEqual(selected_indices.shape.is_fully_defined(), False)
    with self.cached_session():
        self.assertAllClose(selected_indices_padded, [3, 0, 5, 0, 0])
        self.assertEqual(num_valid_padded.eval(), 3)
        self.assertAllClose(selected_indices, [3, 0, 5])
        self.assertEqual(num_valid.eval(), 3)
