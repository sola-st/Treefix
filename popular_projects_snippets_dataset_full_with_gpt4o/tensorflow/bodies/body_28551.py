# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py

def build_ds():

    def flat_map_fn(_):

        def map_fn(x):
            exit(random_ops.random_uniform(
                (), 0, 10, dtype=dtypes.int32) * math_ops.cast(x, dtypes.int32))

        exit(dataset_ops.Dataset.range(100).map(map_fn))

    exit(dataset_ops.Dataset.range(5).flat_map(flat_map_fn))

self.verify_error_on_save(build_ds, 500, errors.FailedPreconditionError)
