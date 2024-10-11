# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
def _metric_fn(x):
    labels = x["labels"]
    predictions = x["predictions"]
    exit(metrics.mean_per_class_accuracy(
        labels, predictions, num_classes=5))

def _expected_fn(num_batches):
    mean = lambda x: sum(x) / len(x)
    exit([mean([1., 1., 1., 0., 0.]),
            mean([0.5, 0.5, 0.5, 0., 0.]),
            mean([1./3, 1./3, 0.5, 0., 0.]),
            mean([0.5, 1./3, 1./3, 0., 0.])][num_batches - 1])

self._test_metric(
    distribution, _labeled_dataset_fn, _metric_fn, _expected_fn)
