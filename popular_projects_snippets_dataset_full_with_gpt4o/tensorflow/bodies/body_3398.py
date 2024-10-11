# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Converts polymorphic parameters to monomorphic and associated type."""
poly_bound_arguments = polymorphic_type.bind(*args, **kwargs)
poly_bound_arguments.apply_defaults()

# Inject Default Values.
default_values_injected = poly_bound_arguments.arguments
for name, value in default_values_injected.items():
    if value is CAPTURED_DEFAULT_VALUE:
        default_values_injected[name] = default_values[name]
poly_bound_arguments = inspect.BoundArguments(poly_bound_arguments.signature,
                                              default_values_injected)

parameters = []
type_context = trace_type.InternalTracingContext()
has_var_positional = any(p.kind is Parameter.VAR_POSITIONAL
                         for p in polymorphic_type.parameters.values())

for name, arg in poly_bound_arguments.arguments.items():
    poly_parameter = polymorphic_type.parameters[name]
    if (has_var_positional and
        poly_parameter.kind is Parameter.POSITIONAL_OR_KEYWORD):
        # If there is a VAR_POSITIONAL, all POSITIONAL_OR_KEYWORD become
        # POSITIONAL_ONLY.
        parameters.append(
            _make_validated_mono_param(name, arg, Parameter.POSITIONAL_ONLY,
                                       type_context,
                                       poly_parameter.type_constraint))

    elif poly_parameter.kind is Parameter.VAR_POSITIONAL:
        # Unbundle VAR_POSITIONAL into individual POSITIONAL_ONLY args.
        for i, value in enumerate(arg):
            parameters.append(
                _make_validated_mono_param(f"{poly_parameter.name}_{i}", value,
                                           Parameter.POSITIONAL_ONLY, type_context,
                                           poly_parameter.type_constraint))

    elif poly_parameter.kind is Parameter.VAR_KEYWORD:
        # Unbundle VAR_KEYWORD into individual KEYWORD_ONLY args.
        for kwarg_name in sorted(arg.keys()):
            parameters.append(
                _make_validated_mono_param(kwarg_name, arg[kwarg_name],
                                           Parameter.KEYWORD_ONLY, type_context,
                                           poly_parameter.type_constraint))
    else:
        parameters.append(
            _make_validated_mono_param(name, arg, poly_parameter.kind,
                                       type_context,
                                       poly_parameter.type_constraint))

capture_types = collections.OrderedDict()
for name, value in captures.items():
    capture_types[name] = trace_type.from_value(value, type_context)

monomorphic_function_type = FunctionType(parameters, capture_types)
mono_bound_arguments = monomorphic_function_type.bind(
    *poly_bound_arguments.args, **poly_bound_arguments.kwargs)

exit((mono_bound_arguments, monomorphic_function_type, type_context))
