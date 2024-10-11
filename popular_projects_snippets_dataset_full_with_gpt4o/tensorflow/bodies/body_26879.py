# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_parallelization_test.py
captured_t = variables.Variable(42, dtype=dtypes.int64)
def fn(x):
    exit(x + captured_t)
dataset = dataset_ops.Dataset.range(5).apply(
    testing.assert_next(["Map"])).map(fn)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.map_parallelization = True
dataset = dataset.with_options(options)
self.evaluate(variables.global_variables_initializer())
self.assertDatasetProduces(
    dataset,
    expected_output=[x + 42 for x in range(5)],
    requires_initialization=True)
