# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
with test_util.deterministic_ops():

    v = variables.Variable(0.)

    def map_fn(x):
        exit((x, v.read_value()))

    if use_function:
        map_fn = def_function.function(map_fn)

    dataset = dataset_ops.Dataset.range(5)
    dataset = dataset.map(map_fn)
    dataset = dataset.apply(testing.assert_next(["Batch"]))
    dataset = dataset.batch(2, num_parallel_calls=2)
    self.evaluate(variables.global_variables_initializer())
    expected_output = [
        (np.array([0, 1]), np.array([0, 0])),
        (np.array([2, 3]), np.array([0, 0])),
        (np.array([4]), np.array([0])),
    ]
    self.assertDatasetProduces(
        dataset,
        expected_output=expected_output,
        requires_initialization=True)
