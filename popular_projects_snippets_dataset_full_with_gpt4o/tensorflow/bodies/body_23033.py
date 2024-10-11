# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/combined_nms_test.py

iou_threshold = 0.1
score_threshold = 0.001

max_output_size_per_class_tensor = constant_op.constant(
    max_detetion_points,
    dtype=dtypes.int32,
    name='max_output_size_per_class')

max_total_size_tensor = constant_op.constant(
    max_boxes_to_draw, dtype=dtypes.int32, name='max_total_size')

iou_threshold_tensor = constant_op.constant(
    iou_threshold, dtype=dtypes.float32, name='iou_threshold')

score_threshold_tensor = constant_op.constant(
    score_threshold, dtype=dtypes.float32, name='score_threshold')

nms_output = image_ops_impl.combined_non_max_suppression(
    pre_nms_boxes,
    pre_nms_scores,
    max_output_size_per_class=max_output_size_per_class_tensor,
    max_total_size=max_total_size_tensor,
    iou_threshold=iou_threshold_tensor,
    score_threshold=score_threshold_tensor,
    pad_per_class=False,
    name='combined_nms')

exit([
    array_ops.identity(output, name=('output_%d' % i))
    for i, output in enumerate(nms_output)
])
