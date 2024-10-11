# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec_test.py

@decorator
def foo(x, y, z=3):  # pylint: disable=unused-argument
    pass

spec = function_spec.FunctionSpec.from_function_and_signature(
    foo, input_signature)
self.assertEqual(
    tuple(spec.fullargspec),
    (['x', 'y', 'z'], None, None, (3,), [], None, {}))
self.assertEqual(spec.is_method, False)
self.assertEqual(spec.input_signature, input_signature)
self.assertEqual(spec.default_values, {'z': 3})
self.assertEqual(
    spec.function_type,
    function_type_lib.FunctionType([
        function_type_lib.Parameter(
            'x', function_type_lib.Parameter.POSITIONAL_OR_KEYWORD, False,
            type_constraint[0]),
        function_type_lib.Parameter(
            'y', function_type_lib.Parameter.POSITIONAL_OR_KEYWORD, False,
            type_constraint[1]),
        function_type_lib.Parameter(
            'z', function_type_lib.Parameter.POSITIONAL_OR_KEYWORD, True,
            type_constraint[2])
    ]))
