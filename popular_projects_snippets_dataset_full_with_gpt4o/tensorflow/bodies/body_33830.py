# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.mean_iou(
    predictions=array_ops.ones([10, 1]),
    labels=array_ops.ones([10, 1]),
    num_classes=2)
_assert_metric_variables(self, ('mean_iou/total_confusion_matrix:0',))
