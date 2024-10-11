# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Checks the python_function to be valid against the input_signature."""
if not callable(python_function):
    raise TypeError(f"{python_function} is not a callable object.")

if input_signature is not None:
    fullargspec = tf_inspect.getfullargspec(python_function)
    if set(fullargspec.kwonlyargs) - set(fullargspec.kwonlydefaults or ()):
        nodefault_kwonlyargs = set(fullargspec.kwonlyargs)
        if fullargspec.kwonlydefaults is not None:
            nodefault_kwonlyargs -= set(fullargspec.kwonlydefaults)
        raise ValueError("Cannot build TF function from "
                         f"{python_function.__name__}: keyword-only arguments "
                         "must have default values when input_signature is "
                         "provided. Got keyword-only arguments without default "
                         f"values: {sorted(nodefault_kwonlyargs)}.")
