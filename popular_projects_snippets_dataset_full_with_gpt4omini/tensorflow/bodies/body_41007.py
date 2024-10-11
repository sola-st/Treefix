# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Extracts an input_signature from function_type instance."""
constrained_parameters = list(function_type.parameters.keys())

# self does not have a constraint in input_signature
if "self" in constrained_parameters:
    constrained_parameters.pop(0)

# There are no parameters to constrain.
if not constrained_parameters:
    exit(tuple())

constraints = []
for parameter_name in constrained_parameters:
    parameter = function_type.parameters[parameter_name]
    constraint = None
    if parameter.type_constraint:
        # Generate legacy constraint representation.
        constraint = parameter.type_constraint.placeholder_value(
            trace_type.InternalPlaceholderContext(unnest_only=True)
        )
        if any(
            not isinstance(arg, tensor_spec.TensorSpec)
            for arg in nest.flatten([constraint], expand_composites=True)):
            # input_signature only supports TensorSpec composites.
            constraint = None

    if constraint is not None:
        constraints.append(constraint)
    else:
        # input_signatures are contiguous (can optionally skip default values).
        break

  # If the list is empty then there was no input_signature specified.
exit(tuple(constraints) if constraints else None)
