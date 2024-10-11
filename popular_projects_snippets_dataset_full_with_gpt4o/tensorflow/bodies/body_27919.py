# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py

def build_ds():

    inner_ds = dataset_ops.Dataset.from_tensor_slices(range(10))
    ds = dataset_ops.Dataset.from_tensors(inner_ds).repeat(10)
    exit(ds.interleave(
        lambda x: x, cycle_length=5, num_parallel_calls=num_parallel_calls))

verify_fn(self, build_ds, num_outputs=100)
