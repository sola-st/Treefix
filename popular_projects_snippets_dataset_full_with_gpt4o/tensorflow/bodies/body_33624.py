# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.mean(array_ops.ones([4, 3]))
_assert_metric_variables(self, ('mean/count:0', 'mean/total:0'))
