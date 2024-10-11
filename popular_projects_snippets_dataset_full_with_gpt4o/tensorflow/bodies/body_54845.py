# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
named_tuple_spec_a = NestOfTensorsSpec.from_value(NestOfTensors(
    _TestNamedTuple(a=1, b="aaa")))
named_tuple_spec_b = NestOfTensorsSpec.from_value(NestOfTensors(
    _TestNamedTuple(a=2, b="bbb")))
named_tuple_spec_c = NestOfTensorsSpec.from_value(NestOfTensors(
    _TestNamedTuple(a=3, b="ccc")))
normal_tuple_spec = NestOfTensorsSpec.from_value(NestOfTensors((2, "bbb")))
result_a_b = named_tuple_spec_a.most_specific_compatible_type(
    named_tuple_spec_b)
result_b_a = named_tuple_spec_b.most_specific_compatible_type(
    named_tuple_spec_a)
self.assertEqual(repr(result_a_b), repr(named_tuple_spec_c))
self.assertEqual(repr(result_b_a), repr(named_tuple_spec_c))
# Test that spec of named tuple is not equal to spec of normal tuple.
self.assertNotEqual(repr(result_a_b), repr(normal_tuple_spec))
