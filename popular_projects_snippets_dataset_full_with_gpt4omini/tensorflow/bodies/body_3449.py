# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py

def foo(*my_var_args):
    del my_var_args

polymorphic_type = function_type.FunctionType.from_callable(foo)
bound_args, mono_type, _ = function_type.canonicalize_to_monomorphic(
    (1, 2, 3), {}, {}, {}, polymorphic_type)

self.assertEqual(bound_args.args, (1, 2, 3))
self.assertEqual(bound_args.kwargs, {})

type_context = trace_type.InternalTracingContext()
expected_type = function_type.FunctionType([
    function_type.Parameter("my_var_args_0",
                            function_type.Parameter.POSITIONAL_ONLY, False,
                            trace_type.from_value(1, type_context)),
    function_type.Parameter("my_var_args_1",
                            function_type.Parameter.POSITIONAL_ONLY, False,
                            trace_type.from_value(2, type_context)),
    function_type.Parameter("my_var_args_2",
                            function_type.Parameter.POSITIONAL_ONLY, False,
                            trace_type.from_value(3, type_context)),
])

self.assertEqual(mono_type, expected_type)
