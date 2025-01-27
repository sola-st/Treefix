# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
tuple_original = default_types.Tuple(
    default_types.Literal(1), default_types.Literal(2),
    default_types.Literal(3))

self.assertEqual(
    serialization.deserialize(serialization.serialize(tuple_original)),
    tuple_original)
