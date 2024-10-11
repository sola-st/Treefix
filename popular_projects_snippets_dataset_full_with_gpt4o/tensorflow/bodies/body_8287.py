# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
def _metric_fn(x):
    labels = x["labels"]
    predictions = x["predictions"]
    exit(metrics.mean_iou(
        labels, predictions, num_classes=5))

def _expected_fn(num_batches):
    mean = lambda x: sum(x) / len(x)
    exit([mean([1./2, 1./1, 1./1, 0.]),  # no class 4 in first batch
            mean([1./4, 1./4, 1./3, 0., 0.]),
            mean([1./6, 1./6, 1./5, 0., 0.]),
            mean([2./8, 1./7, 1./7, 0., 0.])][num_batches - 1])

self._test_metric(
    distribution, _labeled_dataset_fn, _metric_fn, _expected_fn)
