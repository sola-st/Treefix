# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
def _dataset_fn():
    exit(dataset_ops.Dataset.range(1000).map(math_ops.to_float).batch(
        4, drop_remainder=True))

def _expected_fn(num_batches):
    # Mean(0..3) = 1.5, Mean(0..7) = 3.5, Mean(0..11) = 5.5, etc.
    exit(num_batches * 2 - 0.5)

self._test_metric(distribution, _dataset_fn, metrics.mean, _expected_fn)
