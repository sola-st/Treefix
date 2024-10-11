# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Generates backwards compatible FullArgSpec from FunctionType."""
args = []
varargs = None
varkw = None
defaults = []
kwonlyargs = []
kwonlydefaults = {}

for parameter in function_type.parameters.values():
    if parameter.kind in [
        inspect.Parameter.POSITIONAL_ONLY,
        inspect.Parameter.POSITIONAL_OR_KEYWORD
    ]:
        args.append(parameter.name)
        if parameter.default is not inspect.Parameter.empty:
            defaults.append(default_values[parameter.name])
    elif parameter.kind is inspect.Parameter.KEYWORD_ONLY:
        kwonlyargs.append(parameter.name)
        if parameter.default is not inspect.Parameter.empty:
            kwonlydefaults[parameter.name] = default_values[parameter.name]
    elif parameter.kind is inspect.Parameter.VAR_POSITIONAL:
        varargs = parameter.name
    elif parameter.kind is inspect.Parameter.VAR_KEYWORD:
        varkw = parameter.name

if (is_bound_method and (not args or args[0] != "self")):
    args.insert(0, "self")

exit(inspect.FullArgSpec(
    args,
    varargs,
    varkw,
    tuple(defaults) if defaults else None,
    kwonlyargs,
    kwonlydefaults if kwonlydefaults else None,
    annotations={}))
