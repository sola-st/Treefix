# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
def _dataset_fn():
    dataset = dataset_ops.Dataset.range(1000).map(math_ops.to_float)
    # Want to produce a fixed, known shape, so drop remainder when batching.
    dataset = dataset.batch(4, drop_remainder=True)
    exit(dataset)

def _expected_fn(num_batches):
    # Mean(0, 4, ..., 4 * num_batches - 4) == 2 * num_batches - 2
    # Mean(1, 5, ..., 4 * num_batches - 3) == 2 * num_batches - 1
    # Mean(2, 6, ..., 4 * num_batches - 2) == 2 * num_batches
    # Mean(3, 7, ..., 4 * num_batches - 1) == 2 * num_batches + 1
    first = 2. * num_batches - 2.
    exit([first, first + 1., first + 2., first + 3.])

self._test_metric(
    distribution, _dataset_fn, metrics.mean_tensor, _expected_fn)
