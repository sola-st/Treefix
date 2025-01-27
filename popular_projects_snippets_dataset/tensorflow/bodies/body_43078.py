# Extracted from ./data/repos/tensorflow/tensorflow/python/util/variable_utils_test.py
ct = CT()
data = [resource_variable_ops.ResourceVariable(1),
        resource_variable_ops.ResourceVariable(2),
        constant_op.constant(3),
        [4],
        5,
        ct]
if not context.executing_eagerly():
    self.evaluate(variables.global_variables_initializer())

results = variable_utils.convert_variables_to_tensors(data)
expected_results = [1, 2, 3, [4], 5, ct]
# Only ResourceVariables are converted to Tensors.
self.assertIsInstance(results[0], ops.Tensor)
self.assertIsInstance(results[1], ops.Tensor)
self.assertIsInstance(results[2], ops.Tensor)
self.assertIsInstance(results[3], list)
self.assertIsInstance(results[4], int)
self.assertIs(results[5], ct)
results[:3] = self.evaluate(results[:3])
self.assertAllEqual(results, expected_results)
