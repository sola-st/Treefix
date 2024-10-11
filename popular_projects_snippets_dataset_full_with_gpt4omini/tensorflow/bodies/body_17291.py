# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
boxes_np = [[0, 0, 1, 1], [0, 0.1, 1, 1.1], [0, -0.1, 1, 0.9],
            [0, 10, 1, 11], [0, 10.1, 1, 11.1], [0, 100, 1, 101]]
scores_np = [0.9, 0.75, 0.6, 0.95, 0.5, 0.3]
max_output_size_np = 3
iou_threshold_np = 0.5
with self.cached_session():
    boxes = constant_op.constant(boxes_np)
    scores = constant_op.constant(scores_np)
    max_output_size = constant_op.constant(max_output_size_np)
    iou_threshold = constant_op.constant(iou_threshold_np)
    selected_indices = image_ops.non_max_suppression(
        boxes, scores, max_output_size, iou_threshold)
    self.assertAllClose(selected_indices, [3, 0, 5])
