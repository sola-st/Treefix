# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
metrics.auc(predictions=array_ops.ones((10, 1)),
            labels=array_ops.ones((10, 1)))
_assert_metric_variables(self,
                         ('auc/true_positives:0', 'auc/false_negatives:0',
                          'auc/false_positives:0', 'auc/true_negatives:0'))
