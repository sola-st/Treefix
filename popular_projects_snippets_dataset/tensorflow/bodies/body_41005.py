# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Returns default values from the function's inspected fullargspec."""
if fullargspec.defaults is not None:
    defaults = {
        name: value for name, value in zip(
            fullargspec.args[-len(fullargspec.defaults):], fullargspec.defaults)
    }
else:
    defaults = {}

if fullargspec.kwonlydefaults is not None:
    defaults.update(fullargspec.kwonlydefaults)

defaults = {
    function_type_lib.sanitize_arg_name(name): value
    for name, value in defaults.items()
}

exit(defaults)
