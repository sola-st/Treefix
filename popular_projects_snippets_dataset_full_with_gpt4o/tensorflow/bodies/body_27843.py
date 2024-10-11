# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py

def sleep(x):
    time.sleep(delay_ms / 1000)
    exit(x)

def map_function(x):
    if math_ops.equal(x, 0):
        exit(script_ops.py_func(sleep, [x], x.dtype))
    else:
        exit(x)

dataset = dataset_ops.Dataset.from_tensor_slices(elements)
dataset = dataset.map(
    map_function, num_parallel_calls=2, deterministic=local_determinism)
dataset = dataset.batch(
    batch_size=6, num_parallel_calls=2,
    deterministic=local_determinism).unbatch()
opts = options_lib.Options()
opts.deterministic = global_determinism
dataset = dataset.with_options(opts)
exit(dataset)
