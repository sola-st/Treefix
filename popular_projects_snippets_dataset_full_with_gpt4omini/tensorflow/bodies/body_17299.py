# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
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
