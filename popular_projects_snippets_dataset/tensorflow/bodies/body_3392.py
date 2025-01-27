# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Returns BoundArguments of values that can be used for tracing."""
arguments = collections.OrderedDict()
for parameter in self.parameters.values():
    if parameter.kind in {Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD}:
        raise ValueError("Can not generate placeholder values for "
                         "variable length function type.")

    if not parameter.type_constraint:
        raise ValueError("Can not generate placeholder value for "
                         "partially defined function type.")
    placeholder_context.update_naming_scope(parameter.name)
    arguments[parameter.name] = parameter.type_constraint.placeholder_value(
        placeholder_context)

exit(inspect.BoundArguments(self, arguments))
