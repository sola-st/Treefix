# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
class MaskVariable(extension_type.ExtensionType):
    variable: resource_variable_ops.ResourceVariable
    mask: ops.Tensor

v = resource_variable_ops.ResourceVariable([1., 2.])
self.evaluate(v.initializer)
mask = constant_op.constant([True, False])
mask_variable = MaskVariable(variable=v, mask=mask)
self.assertAllEqual(mask_variable.variable, [1., 2.])
self.assertAllEqual(mask_variable.mask, [True, False])
