# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Adds type constraints to a FunctionType based on the input_signature."""
context = trace_type.InternalTracingContext(is_legacy_signature=True)
constraints = [trace_type.from_value(c, context) for c in input_signature]
parameters = []

has_var_pos = any(
    p.kind is p.VAR_POSITIONAL for p in function_type.parameters.values())

for param in function_type.parameters.values():
    # VAR_POSITIONAL does not allow POSITIONAL_OR_KEYWORD args.
    sanitized_kind = (
        param.POSITIONAL_ONLY if has_var_pos and
        param.kind is param.POSITIONAL_OR_KEYWORD else param.kind)

    if param.name == "self":
        # Type constraints do not apply on them.
        parameters.append(Parameter("self", sanitized_kind, param.optional, None))

    elif param.kind is param.VAR_KEYWORD:
        # Disabled when input_signature is specified.
        continue

    elif param.kind is param.VAR_POSITIONAL:
        # Convert into Positional Only args based on length of constraints.
        for i in range(len(constraints)):
            parameters.append(
                Parameter(param.name + "_" + str(i), Parameter.POSITIONAL_ONLY,
                          False, constraints.pop(0)))

    elif (param.kind in [
        param.POSITIONAL_ONLY, param.POSITIONAL_OR_KEYWORD, param.KEYWORD_ONLY
    ]):
        if constraints:
            parameters.append(
                Parameter(param.name, sanitized_kind, param.optional,
                          constraints.pop(0)))
        elif param.name in default_values:
            type_constraint = trace_type.from_value(default_values[param.name])
            parameters.append(
                Parameter(param.name, sanitized_kind, param.optional,
                          type_constraint))
        else:
            raise TypeError(
                f"input_signature missing type constraint for {param.name}")

if constraints:
    raise TypeError(
        f"input_signature contains {len(constraints)} extra type constraints.")

exit(FunctionType(parameters))
