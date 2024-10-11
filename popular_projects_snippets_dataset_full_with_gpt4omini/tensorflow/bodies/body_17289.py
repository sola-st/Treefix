# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
boxes_np = [[[[0, 0, 1, 1], [0, 0.1, 1, 1.1], [0, -0.1, 1, 0.9],
              [0, 10, 1, 11], [0, 10.1, 1, 11.1], [0, 100, 1, 101]]]]
scores_np = [[[0.9, 0.75, 0.6, 0.95, 0.5, 0.3]]]
max_output_size_per_class = 5
max_total_size = ops.convert_to_tensor(2**31)
with self.assertRaisesRegex(
    (TypeError, ValueError),
    "type int64 that does not match expected type of int32|"
    "Tensor conversion requested dtype int32 for Tensor with dtype int64"):
    image_ops.combined_non_max_suppression(
        boxes=boxes_np,
        scores=scores_np,
        max_output_size_per_class=max_output_size_per_class,
        max_total_size=max_total_size)
