# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
def _metric_fn(x):
    labels = x["labels"]
    predictions = x["predictions"]
    exit(metrics.false_negatives_at_thresholds(labels, predictions, [.5]))

def _expected_fn(num_batches):
    exit([[1.], [1.], [2.], [3.]][num_batches - 1])

self._test_metric(
    distribution, _threshold_dataset_fn, _metric_fn, _expected_fn)
