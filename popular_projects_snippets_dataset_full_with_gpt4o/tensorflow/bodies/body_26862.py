# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/noop_elimination_test.py
"""Runs a noop elimination test case.

    Args:
      init_dataset_fn: Function to create the initial dataset
      transformation: Transformation to apply
      expected_name: Name of the transformation if it is not eliminated
    """
dataset = init_dataset_fn()

if expected_name:
    dataset = dataset.apply(
        testing.assert_next([expected_name, "FiniteTake"]))
else:
    dataset = dataset.apply(testing.assert_next(["FiniteTake"]))

dataset = dataset.apply(transformation)
dataset = dataset.take(1)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.noop_elimination = True
dataset = dataset.with_options(options)

# Run the first iteration for the side effect of checking the assertion.
get_next = self.getNext(dataset)
self.evaluate(get_next())
