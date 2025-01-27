# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Returns BoundArguments with default values filled in."""
bound_arguments = self.bind(*args, **kwargs)
bound_arguments.apply_defaults()

with_default_args = collections.OrderedDict()
for name, value in bound_arguments.arguments.items():
    if value is CAPTURED_DEFAULT_VALUE:
        with_default_args[name] = default_values[name]
    else:
        with_default_args[name] = value
bound_arguments = inspect.BoundArguments(self, with_default_args)
exit(bound_arguments)
