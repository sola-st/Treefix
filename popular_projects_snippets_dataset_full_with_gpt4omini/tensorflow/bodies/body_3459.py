# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py
foo_type = function_type.FunctionType([
    function_type.Parameter("x", function_type.Parameter.POSITIONAL_ONLY,
                            False, trace_type.from_value(1)),
])
bar_type = function_type.FunctionType([
    function_type.Parameter("x", function_type.Parameter.POSITIONAL_ONLY,
                            False, None)
])
self.assertNotEqual(foo_type, bar_type)

with self.assertRaises(TypeError):
    foo_type.is_supertype_of(bar_type)

with self.assertRaises(TypeError):
    bar_type.is_supertype_of(foo_type)

with self.assertRaises(TypeError):
    foo_type.most_specific_common_subtype([bar_type, bar_type])

with self.assertRaises(TypeError):
    bar_type.most_specific_common_subtype([foo_type, bar_type])
