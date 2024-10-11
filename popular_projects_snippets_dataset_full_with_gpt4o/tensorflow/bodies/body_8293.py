# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
def _metric_fn(x):
    labels = x["labels"]
    predictions = x["predictions"]
    exit(metrics.auc(labels, predictions, num_thresholds=8, curve="ROC",
                       summation_method="careful_interpolation"))

def _expected_fn(num_batches):
    exit([0.5, 7./9, 0.8, 0.75][num_batches - 1])

self._test_metric(
    distribution, _threshold_dataset_fn, _metric_fn, _expected_fn)
