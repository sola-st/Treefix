# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
def _metric_fn(x):
    labels = x["labels"]
    predictions = x["predictions"]
    exit(metrics.mean_squared_error(labels, predictions))

def _expected_fn(num_batches):
    exit([0., 1./32, 0.208333, 0.15625][num_batches - 1])

self._test_metric(
    distribution, _regression_dataset_fn, _metric_fn, _expected_fn)
