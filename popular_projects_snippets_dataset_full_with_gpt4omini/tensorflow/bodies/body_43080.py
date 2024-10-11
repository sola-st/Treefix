# Extracted from ./data/repos/tensorflow/tensorflow/python/util/variable_utils_test.py
data = [resource_variable_ops.ResourceVariable(1),
        resource_variable_ops.ResourceVariable(2),
        constant_op.constant(3),
        [4],
        5]
if not context.executing_eagerly():
    self.evaluate(variables.global_variables_initializer())

results = variable_utils.replace_variables_with_atoms(data)
expected_results = [0, 0, 3, [4], 5]
# Only ResourceVariables are replaced with int 0s.
self.assertIsInstance(results[0], int)
self.assertIsInstance(results[1], int)
self.assertIsInstance(results[2], ops.Tensor)
self.assertIsInstance(results[3], list)
self.assertIsInstance(results[4], int)
results[2] = self.evaluate(results[2])
self.assertAllEqual(results, expected_results)

# Make sure 0 is a tf.nest atom with expand_composites=True.
flat_results = nest.flatten(results, expand_composites=True)
expected_flat_results = [0, 0, 3, 4, 5]
self.assertAllEqual(flat_results, expected_flat_results)
