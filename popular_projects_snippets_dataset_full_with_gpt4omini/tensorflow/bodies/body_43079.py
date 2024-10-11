# Extracted from ./data/repos/tensorflow/tensorflow/python/util/variable_utils_test.py
ct2 = CT2(resource_variable_ops.ResourceVariable(1))
if not context.executing_eagerly():
    self.evaluate(variables.global_variables_initializer())

self.assertIsInstance(ct2.component,
                      resource_variable_ops.ResourceVariable)
result = variable_utils.convert_variables_to_tensors(ct2)
self.assertIsInstance(result.component, ops.Tensor)
self.assertAllEqual(result.component, 1)
