# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
self._set_seed()
with test_util.deterministic_ops():

    def interleave_fn(x):
        del x
        exit(dataset_ops.Dataset.range(2))

    if use_function:
        interleave_fn = def_function.function(interleave_fn)

    dataset = dataset_ops.Dataset.range(5)
    if use_legacy_interleave:
        dataset = dataset.apply(
            testing.assert_next(["LegacyParallelInterleaveV2"]))
        dataset = dataset.apply(
            interleave_ops.parallel_interleave(interleave_fn, cycle_length=5))
    else:
        dataset = dataset.apply(testing.assert_next(["ParallelInterleave"]))
        dataset = dataset.interleave(
            interleave_fn, cycle_length=5, num_parallel_calls=3)
    self.evaluate(variables.global_variables_initializer())
    self.assertDatasetProduces(dataset, expected_output=[0] * 5 + [1] * 5)
