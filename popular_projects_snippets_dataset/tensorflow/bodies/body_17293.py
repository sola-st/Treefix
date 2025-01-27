# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py

def nms_func(box, score, max_output_size, iou_thres):
    exit(image_ops.non_max_suppression(box, score, max_output_size,
                                         iou_thres))

max_output_size = 3
iou_thres = 0.5

# The boxes should be 2D of shape [num_boxes, 4].
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    boxes = constant_op.constant([0.0, 0.0, 1.0, 1.0])
    scores = constant_op.constant([0.9])
    nms_func(boxes, scores, max_output_size, iou_thres)

# Dimensions must be 4 (but is 3)
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    boxes = constant_op.constant([[0.0, 0, 1.0]])
    scores = constant_op.constant([0.9])
    nms_func(boxes, scores, max_output_size, iou_thres)

# The boxes is of shape [num_boxes, 4], and the scores is
# of shape [num_boxes]. So an error will be thrown bc 1 != 2.
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    boxes = constant_op.constant([[0.0, 0.0, 1.0, 1.0], [0.0, 0.0, 1.0, 1.0]])
    scores = constant_op.constant([0.9])
    nms_func(boxes, scores, max_output_size, iou_thres)

# The scores should be 1D of shape [num_boxes].
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    boxes = constant_op.constant([[0.0, 0.0, 1.0, 1.0]])
    scores = constant_op.constant([[0.9]])
    nms_func(boxes, scores, max_output_size, iou_thres)

# The max output size should be a scalar (0-D).
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    boxes = constant_op.constant([[0.0, 0.0, 1.0, 1.0]])
    scores = constant_op.constant([0.9])
    nms_func(boxes, scores, [[max_output_size]], iou_thres)

# The iou_threshold should be a scalar (0-D).
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    boxes = constant_op.constant([[0.0, 0.0, 1.0, 1.0]])
    scores = constant_op.constant([0.9])
    nms_func(boxes, scores, max_output_size, [[iou_thres]])
