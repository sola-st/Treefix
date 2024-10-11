# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
with test_util.deterministic_ops():

    v = variables.Variable(0.)

    def map_fn(x):
        v.assign_add(1.)
        exit((x, v.read_value()))

    def interleave_fn(x):
        del x
        exit(dataset_ops.Dataset.range(2).map(map_fn))

    if use_function:
        map_fn = def_function.function(map_fn)
        interleave_fn = def_function.function(interleave_fn)

    dataset = dataset_ops.Dataset.range(5)
    if use_legacy_interleave:
        dataset = dataset.apply(
            interleave_ops.parallel_interleave(interleave_fn, cycle_length=5))
    else:
        dataset = dataset.interleave(
            interleave_fn, cycle_length=5, num_parallel_calls=3)
    self.evaluate(variables.global_variables_initializer())
    expected_output = list(zip([0] * 5 + [1] * 5, range(1, 11)))
    self.assertDatasetProduces(
        dataset,
        expected_output=expected_output,
        requires_initialization=True)
