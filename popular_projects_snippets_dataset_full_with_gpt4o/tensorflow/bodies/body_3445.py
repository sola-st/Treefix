# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py

def foo(x=1, y=2, z=3):
    del x, y, z

polymorphic_type = function_type.FunctionType.from_callable(foo)
bound_args, mono_type, _ = function_type.canonicalize_to_monomorphic(
    args, kwargs, function_type.FunctionType.get_default_values(foo), {},
    polymorphic_type)

self.assertEqual(bound_args.args, (1, 2, 3))
self.assertEqual(bound_args.kwargs, {})

type_context = trace_type.InternalTracingContext()
expected_type = function_type.FunctionType([
    function_type.Parameter("x",
                            function_type.Parameter.POSITIONAL_OR_KEYWORD,
                            False, trace_type.from_value(1, type_context)),
    function_type.Parameter("y",
                            function_type.Parameter.POSITIONAL_OR_KEYWORD,
                            False, trace_type.from_value(2, type_context)),
    function_type.Parameter("z",
                            function_type.Parameter.POSITIONAL_OR_KEYWORD,
                            False, trace_type.from_value(3, type_context)),
])

self.assertEqual(mono_type, expected_type)
