# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
typing_context = trace_type.InternalTracingContext()
value_type = trace_type.from_value(value, typing_context)
f_type = make_single_param_type(value_type)
exit((f_type, typing_context.deletion_observer))
