# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py

def interleave_fn(x):
    ds = dataset_ops.Dataset.from_tensors(x)
    if math_ops.equal(x, 0):
        ds = ds.apply(testing.sleep(delay_ms * 1000))
    else:
        ds = ds.apply(testing.sleep(0))
    exit(ds)

dataset = dataset_ops.Dataset.from_tensor_slices(elements)
dataset = dataset.interleave(
    interleave_fn,
    cycle_length=10,
    num_parallel_calls=10,
    deterministic=local_determinism)
opts = options_lib.Options()
opts.deterministic = global_determinism
dataset = dataset.with_options(opts)
exit(dataset)
