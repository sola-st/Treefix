# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.mean_tensor(array_ops.ones([4, 3]))
_assert_metric_variables(self,
                         ('mean/total_tensor:0', 'mean/count_tensor:0'))
