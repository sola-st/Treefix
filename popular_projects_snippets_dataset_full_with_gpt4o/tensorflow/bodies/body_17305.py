# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
overlaps_np = [
    [1.0, 0.7, 0.2],
    [0.7, 1.0, 0.0],
    [0.2, 0.0, 1.0],
]
scores_np = [0.7, 0.9, 0.1]
max_output_size_np = 3

overlaps = constant_op.constant(overlaps_np)
scores = constant_op.constant(scores_np)
max_output_size = constant_op.constant(max_output_size_np)
overlap_threshold = 0.6
score_threshold = 0.4

selected_indices = image_ops.non_max_suppression_with_overlaps(
    overlaps, scores, max_output_size, overlap_threshold, score_threshold)

with self.cached_session():
    self.assertAllClose(selected_indices, [1])
