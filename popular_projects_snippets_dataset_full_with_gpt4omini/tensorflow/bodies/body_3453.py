# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py

def foo(*args, **kwargs):
    del args, kwargs

polymorphic_type = function_type.FunctionType.from_callable(foo)
bound_args, mono_type, _ = function_type.canonicalize_to_monomorphic((1,), {
    "y": 2,
    "z": 3
}, {}, {}, polymorphic_type)

self.assertEqual(bound_args.args, (1,))
self.assertEqual(bound_args.kwargs, {"y": 2, "z": 3})

type_context = trace_type.InternalTracingContext()
expected_type = function_type.FunctionType([
    function_type.Parameter("args_0",
                            function_type.Parameter.POSITIONAL_ONLY, False,
                            trace_type.from_value(1, type_context)),
    function_type.Parameter("y", function_type.Parameter.KEYWORD_ONLY,
                            False, trace_type.from_value(2, type_context)),
    function_type.Parameter("z", function_type.Parameter.KEYWORD_ONLY,
                            False, trace_type.from_value(3, type_context)),
])

self.assertEqual(mono_type, expected_type)
