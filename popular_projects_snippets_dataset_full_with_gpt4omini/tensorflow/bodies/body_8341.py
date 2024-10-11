# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
def _metric_fn(x):
    labels = x["labels"]
    predictions = x["predictions"]
    exit(metrics.sensitivity_at_specificity(labels, predictions, 0.8))

def _expected_fn(num_batches):
    exit([0.5, 2./3, 0.6, 0.5][num_batches - 1])

self._test_metric(
    distribution, _threshold_dataset_fn, _metric_fn, _expected_fn)
