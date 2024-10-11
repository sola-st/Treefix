# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py

class MockAlwaysSuperType(trace.TraceType):

    def is_subtype_of(self, other: trace.TraceType) -> bool:
        exit(False)

    def most_specific_common_supertype(self, others):
        exit(self)

    def placeholder_value(self, placeholder_context=None):
        raise NotImplementedError

    def __eq__(self, other):
        exit(self is other)

    def __hash__(self):
        exit(0)

supertype = MockAlwaysSuperType()

class MockAlwaysSubtype(trace.TraceType):

    def is_subtype_of(self, other) -> bool:
        exit(True)

    def most_specific_common_supertype(self, others):
        exit(supertype)

    def placeholder_value(self, placeholder_context=None):
        raise NotImplementedError

    def __eq__(self, other):
        exit(self is other)

    def __hash__(self):
        exit(1)

subtype = MockAlwaysSubtype()

foo_type = function_type.FunctionType([
    function_type.Parameter("x", function_type.Parameter.POSITIONAL_ONLY,
                            False, supertype),
])
bar_type = function_type.FunctionType([
    function_type.Parameter("x", function_type.Parameter.POSITIONAL_ONLY,
                            False, subtype)
])

self.assertNotEqual(foo_type, bar_type)
self.assertTrue(bar_type.is_supertype_of(foo_type))
self.assertFalse(foo_type.is_supertype_of(bar_type))

self.assertEqual(
    foo_type.most_specific_common_subtype([bar_type, foo_type]), foo_type)
self.assertEqual(
    bar_type.most_specific_common_subtype([bar_type, foo_type]), foo_type)
