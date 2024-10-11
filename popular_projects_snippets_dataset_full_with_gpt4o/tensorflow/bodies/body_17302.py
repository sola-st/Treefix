# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
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
