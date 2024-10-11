# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
boxes_np = [[0, 0, 1, 1], [0, 0.1, 1, 1.1], [0, -0.1, 1, 0.9],
            [0, 10, 1, 11], [0, 10.1, 1, 11.1], [0, 100, 1, 101]]
scores_np = [0.9, 0.75, 0.6, 0.95, 0.5, 0.3]
max_output_size_np = 6
iou_threshold_np = 0.5
score_threshold_np = 0.0
soft_nms_sigma_np = 0.5
boxes = constant_op.constant(boxes_np)
scores = constant_op.constant(scores_np)
max_output_size = constant_op.constant(max_output_size_np)
iou_threshold = constant_op.constant(iou_threshold_np)
score_threshold = constant_op.constant(score_threshold_np)
soft_nms_sigma = constant_op.constant(soft_nms_sigma_np)
selected_indices, selected_scores = \
        image_ops.non_max_suppression_with_scores(
        boxes,
        scores,
        max_output_size,
        iou_threshold,
        score_threshold,
        soft_nms_sigma)
selected_indices, selected_scores = self.evaluate(
    [selected_indices, selected_scores])
self.assertAllClose(selected_indices, [3, 0, 1, 5, 4, 2])
self.assertAllClose(selected_scores,
                    [0.95, 0.9, 0.384, 0.3, 0.256, 0.197],
                    rtol=1e-2, atol=1e-2)
