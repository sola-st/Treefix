# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py
foo_type = function_type.FunctionType([
    function_type.Parameter("x", function_type.Parameter.POSITIONAL_ONLY,
                            False, trace_type.from_value(1))
])
self.assertEqual(foo_type, foo_type)
self.assertTrue(foo_type.is_supertype_of(foo_type))
self.assertEqual(
    foo_type,
    foo_type.most_specific_common_subtype([foo_type, foo_type, foo_type]))
