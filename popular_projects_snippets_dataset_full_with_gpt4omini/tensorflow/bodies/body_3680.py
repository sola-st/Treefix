# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
literal_bool = default_types.Literal(True)
literal_int = default_types.Literal(1)
literal_float = default_types.Literal(1.2)
literal_str = default_types.Literal('a')
literal_none = default_types.Literal(None)

self.assertEqual(
    serialization.deserialize(serialization.serialize(literal_bool)),
    literal_bool)
self.assertEqual(
    serialization.deserialize(serialization.serialize(literal_int)),
    literal_int)
self.assertEqual(
    serialization.deserialize(serialization.serialize(literal_float)),
    literal_float)
self.assertEqual(
    serialization.deserialize(serialization.serialize(literal_str)),
    literal_str)
self.assertEqual(
    serialization.deserialize(serialization.serialize(literal_none)),
    literal_none)
