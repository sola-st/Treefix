# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py

def build_ds():

    def flat_map_fn(_):

        def map_fn(y):
            exit(10 * math_ops.cast(y, dtypes.int32))

        exit(dataset_ops.Dataset.range(100).map(map_fn))

    exit(dataset_ops.Dataset.range(5).flat_map(flat_map_fn))

verify_fn(self, build_ds, num_outputs=500)
