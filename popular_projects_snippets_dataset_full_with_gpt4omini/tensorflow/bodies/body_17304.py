# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
boxes_np = [[4.0, 6.0, 3.0, 6.0],
            [2.0, 1.0, 5.0, 4.0],
            [9.0, 0.0, 9.0, 9.0]]
scores = [5.0, 6.0, 5.0]
max_output_size = 2**31
with self.assertRaisesRegex(
    (TypeError, ValueError), "type int64 that does not match type int32"):
    boxes = constant_op.constant(boxes_np)
    image_ops.non_max_suppression_padded(boxes, scores, max_output_size)
