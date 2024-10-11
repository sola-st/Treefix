# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.accuracy(
    predictions=array_ops.ones((10, 1)),
    labels=array_ops.ones((10, 1)),
    name='my_accuracy')
_assert_metric_variables(self,
                         ('my_accuracy/count:0', 'my_accuracy/total:0'))
