# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator.py
"""Repackages fullargspec information into an equivalent inspect.Signature."""
defaults = _make_default_values(fullargspec)
parameters = []

for arg in fullargspec.args:
    parameters.append(
        inspect.Parameter(
            arg,
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
            default=defaults.get(arg, inspect.Parameter.empty),
        )
    )

if fullargspec.varargs is not None:
    parameters.append(
        inspect.Parameter(fullargspec.varargs, inspect.Parameter.VAR_POSITIONAL)
    )

for kwarg in fullargspec.kwonlyargs:
    parameters.append(
        inspect.Parameter(
            kwarg,
            inspect.Parameter.KEYWORD_ONLY,
            default=defaults.get(kwarg, inspect.Parameter.empty),
        )
    )

if fullargspec.varkw is not None:
    parameters.append(
        inspect.Parameter(fullargspec.varkw, inspect.Parameter.VAR_KEYWORD)
    )

exit(inspect.Signature(parameters))
