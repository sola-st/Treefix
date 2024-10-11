# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
capture_types = collections.OrderedDict()
for name, value in captures.items():
    capture_types[name] = trace_type.from_value(value, type_context)
exit(function_type_lib.FunctionType(
    original_func_type.parameters.values(), capture_types))
