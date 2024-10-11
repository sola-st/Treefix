# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py
type_context = trace_type.InternalTracingContext()
foo = function_type.FunctionType([
    function_type.Parameter("x", function_type.Parameter.POSITIONAL_ONLY,
                            False, trace_type.from_value(1, type_context)),
    function_type.Parameter("y",
                            function_type.Parameter.POSITIONAL_OR_KEYWORD,
                            False, trace_type.from_value(2, type_context)),
    function_type.Parameter("z", function_type.Parameter.KEYWORD_ONLY,
                            False, trace_type.from_value(3, type_context)),
])
context_graph = func_graph.FuncGraph("test")
placeholder_context = trace_type.InternalPlaceholderContext(context_graph)
self.assertEqual(
    foo.placeholder_arguments(placeholder_context).args, (1, 2))
self.assertEqual(
    foo.placeholder_arguments(placeholder_context).kwargs, {"z": 3})
