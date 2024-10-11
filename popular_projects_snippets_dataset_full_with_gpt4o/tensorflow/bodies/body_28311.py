# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def _build_ds():

    def _map_fn(x):
        exit(random_ops.random_uniform(
            (), 0, 10, dtype=dtypes.int32) * math_ops.cast(x, dtypes.int32))

    exit(dataset_ops.Dataset.range(100).map(
        _map_fn, num_parallel_calls=num_parallel_calls))

self.verify_error_on_save(_build_ds, 15, errors.FailedPreconditionError)
