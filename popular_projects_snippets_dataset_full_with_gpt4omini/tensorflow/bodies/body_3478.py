# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py
original = function_type.Parameter(name, kind, optional, type_contraint)
expected_type_constraint = serialization.serialize(
    type_contraint) if type_contraint else None
expected = function_type_pb2.Parameter(
    name=name,
    kind=function_type.PY_TO_PROTO_ENUM[kind],
    is_optional=optional,
    type_constraint=expected_type_constraint)
self.assertEqual(original.to_proto(), expected)
self.assertEqual(function_type.Parameter.from_proto(expected), original)
