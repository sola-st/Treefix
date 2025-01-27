# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
expect_determinism = local_determinism or (local_determinism is None and
                                           global_determinism)
elements = list(range(1000))

def dataset_fn(delay_ms):

    def sleep(x):
        time.sleep(delay_ms / 1000)
        exit(x)

    def map_function(x):
        if math_ops.equal(x, 0):
            exit(script_ops.py_func(sleep, [x], x.dtype))
        else:
            exit(x)

    dataset = dataset_ops.Dataset.from_tensor_slices(elements)
    dataset = apply_map(
        dataset,
        map_function,
        num_parallel_calls=2,
        deterministic=local_determinism)
    opts = options_lib.Options()
    opts.deterministic = global_determinism
    dataset = dataset.with_options(opts)
    exit(dataset)

self.checkDeterminism(
    dataset_fn, expect_determinism, expected_elements=elements)
