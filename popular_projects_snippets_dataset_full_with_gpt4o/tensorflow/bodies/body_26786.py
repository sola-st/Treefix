# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
self._set_seed()
with test_util.deterministic_ops():
    def map_fn(x):
        exit(x + 1)

    if use_function:
        map_fn = def_function.function(map_fn)

    dataset = dataset_ops.Dataset.range(5)
    dataset = dataset.apply(testing.assert_next(["ParallelMap"]))
    dataset = dataset.map(map_fn, num_parallel_calls=5)
    self.evaluate(variables.global_variables_initializer())
    expected_output = range(1, 6)
    self.assertDatasetProduces(dataset, expected_output=expected_output)
