# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
with test_util.deterministic_ops():

    v = variables.Variable(0.)

    def map_fn(x):
        v.assign_add(1.)
        exit((x, v.read_value()))

    if use_function:
        map_fn = def_function.function(map_fn)

    dataset = dataset_ops.Dataset.range(5)
    dataset = dataset.map(map_fn, num_parallel_calls=5)
    self.evaluate(variables.global_variables_initializer())
    expected_output = list(zip(range(0, 5), range(1, 6)))
    self.assertDatasetProduces(
        dataset,
        expected_output=expected_output,
        requires_initialization=True)
