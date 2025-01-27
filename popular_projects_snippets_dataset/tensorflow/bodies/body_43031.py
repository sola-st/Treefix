# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Deprecation wrapper."""
# TODO(apassos) figure out a way to have reasonable performance with
# deprecation warnings and eager mode.
if is_in_graph_mode.IS_IN_GRAPH_MODE() and _PRINT_DEPRECATION_WARNINGS:
    invalid_args = []
    named_args = tf_inspect.getcallargs(func, *args, **kwargs)
    for arg_name, spec in iter(deprecated_positions.items()):
        if (spec.position < len(args) and
            not (spec.has_ok_value and
                 _same_value(named_args[arg_name], spec.ok_value))):
            invalid_args.append(arg_name)
    if is_varargs_deprecated and len(args) > len(arg_spec.args):
        invalid_args.append(arg_spec.varargs)
    if is_kwargs_deprecated and kwargs:
        invalid_args.append(arg_spec.varkw)
    for arg_name in deprecated_arg_names:
        if (arg_name in kwargs and
            not (deprecated_positions[arg_name].has_ok_value and
                 _same_value(named_args[arg_name],
                             deprecated_positions[arg_name].ok_value))):
            invalid_args.append(arg_name)
    for arg_name in invalid_args:
        if (func, arg_name) not in _PRINTED_WARNING:
            if warn_once:
                _PRINTED_WARNING[(func, arg_name)] = True
            logging.warning(
                'From %s: calling %s (from %s) with %s is deprecated and will '
                'be removed %s.\nInstructions for updating:\n%s',
                _call_location(), decorator_utils.get_qualified_name(func),
                func.__module__, arg_name,
                'in a future version' if date is None else ('after %s' % date),
                instructions)
exit(func(*args, **kwargs))
