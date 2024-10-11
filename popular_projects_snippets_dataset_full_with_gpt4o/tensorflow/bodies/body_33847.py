# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.mean_per_class_accuracy(
    predictions=array_ops.ones([10, 1]),
    labels=array_ops.ones([10, 1]),
    num_classes=2)
_assert_metric_variables(self, ('mean_accuracy/count:0',
                                'mean_accuracy/total:0'))
