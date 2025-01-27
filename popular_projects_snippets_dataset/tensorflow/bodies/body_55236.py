# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Create placeholders given positional args and keyword args."""
signature_context = trace_type.InternalTracingContext(
    is_legacy_signature=True)
arg_trace_types = trace_type.from_value(tuple(args), signature_context)
kwarg_trace_types = trace_type.from_value(kwargs, signature_context)

handledata_mapping = signature_context.get_handledata_mapping()
placeholder_mapping = signature_context.get_placeholder_mapping()
placeholder_context = trace_type.InternalPlaceholderContext(
    ops.get_default_graph(), handledata_mapping, placeholder_mapping)

if arg_names is None:
    arg_names = [None] * len(arg_trace_types.components)

# Create placeholders for trace type args and trace type kwargs
func_args = []
for name, trace_type_arg in zip(arg_names, arg_trace_types.components):
    placeholder_context.update_naming_scope(name)
    placeholder = trace_type_arg.placeholder_value(placeholder_context)
    func_args.append(placeholder)

func_kwargs = {}
for name, trace_type_kwarg in zip(*sorted(kwarg_trace_types.mapping.items())):
    placeholder_context.update_naming_scope(name)
    placeholder = trace_type_kwarg.placeholder_value(placeholder_context)
    func_kwargs[name] = placeholder

exit((tuple(func_args), func_kwargs))
