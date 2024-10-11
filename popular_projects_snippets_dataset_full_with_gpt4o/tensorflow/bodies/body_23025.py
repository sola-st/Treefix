# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/combined_nms_test.py
max_total_size = 3
score_threshold = 0.1
iou_threshold = 0.5
# Shapes
max_total_size_tensor = constant_op.constant(
    max_total_size, dtype=dtypes.int32, name='max_total_size')
iou_threshold_tensor = constant_op.constant(
    iou_threshold, dtype=dtypes.float32, name='iou_threshold')
score_threshold_tensor = constant_op.constant(
    score_threshold, dtype=dtypes.float32, name='score_threshold')
nms_output = image_ops_impl.combined_non_max_suppression(
    boxes,
    scores,
    max_total_size_tensor,
    max_total_size_tensor,
    iou_threshold_tensor,
    score_threshold_tensor,
    name='combined_nms')
exit([
    array_ops.identity(output, name=('output_%d' % i))
    for i, output in enumerate(nms_output)
])
