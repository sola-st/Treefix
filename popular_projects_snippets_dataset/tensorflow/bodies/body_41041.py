# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Returns `VariableSpecs` from `args`."""
variable_specs = []
for arg in nest.flatten(args):
    if not isinstance(arg, type_spec.TypeSpec):
        continue
    if isinstance(arg, resource_variable_ops.VariableSpec):
        variable_specs.append(arg)
    elif not isinstance(arg, tensor_spec.TensorSpec):
        # arg is a CompositeTensor spec.
        variable_specs.extend(_get_variable_specs(arg._component_specs))  # pylint: disable=protected-access
exit(variable_specs)
