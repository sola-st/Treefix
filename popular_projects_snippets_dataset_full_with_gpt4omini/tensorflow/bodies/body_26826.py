# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
"""Tests that default optimizations are disabled with ref variables."""
variable = variable_scope.get_variable(
    "v", initializer=0, use_resource=False)
assign_op = variable.assign_add(1)
unoptimized_dataset = dataset_fn(variable)

options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.noop_elimination = True
options.experimental_optimization.map_and_batch_fusion = True
optimized_dataset = unoptimized_dataset.with_options(options)
optimized_it = dataset_ops.make_initializable_iterator(optimized_dataset)

# Check that outputs are the same in the optimized and unoptimized cases,
# when the variable value is changing.
unoptimized_it = dataset_ops.make_initializable_iterator(
    unoptimized_dataset)
with ops.control_dependencies([assign_op]):
    unoptimized_output = unoptimized_it.get_next()
    optimized_output = optimized_it.get_next()

self.evaluate(variable.initializer)
self.evaluate((unoptimized_it.initializer, optimized_it.initializer))
while True:
    try:
        unoptimized, optimized = self.evaluate((unoptimized_output,
                                                optimized_output))
        self.assertEqual(unoptimized, optimized)
    except errors.OutOfRangeError:
        break
