# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py
original = function_type.FunctionType([
    function_type.Parameter("a", function_type.Parameter.POSITIONAL_ONLY,
                            False, None),
], collections.OrderedDict([("b", trace_type.from_value(1))]))
expected = function_type_pb2.FunctionType(
    parameters=[
        function_type_pb2.Parameter(
            name="a",
            kind=function_type_pb2.Parameter.Kind.POSITIONAL_ONLY,
            is_optional=False)
    ],
    captures=[
        function_type_pb2.Capture(
            name="b",
            type_constraint=serialization.serialize(
                trace_type.from_value(1)))
    ])
self.assertEqual(original.to_proto(), expected)
self.assertEqual(function_type.FunctionType.from_proto(expected), original)
