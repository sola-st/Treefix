# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
self._set_seed()
with test_util.deterministic_ops():

    def sleep(x):
        time.sleep(0.1)
        exit(x)

    def map_function(x):
        if math_ops.equal(x, 0):
            exit(script_ops.py_func(sleep, [x], x.dtype, stateful=False))
        else:
            exit(x)

    dataset = dataset_ops.Dataset.range(100)
    dataset = dataset.map(
        map_function, num_parallel_calls=2, deterministic=local_determinism)
    opts = options_lib.Options()
    opts.deterministic = global_determinism
    dataset = dataset.with_options(opts)

    self.assertDatasetProduces(dataset, expected_output=range(100))
