# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec_test.py

class MyClass:

    @decorator
    def foo(self, x, y=1):
        pass

spec = function_spec.FunctionSpec.from_function_and_signature(
    MyClass.foo, input_signature)
self.assertEqual(
    tuple(spec.fullargspec),
    (['self', 'x', 'y'], None, None, (1,), [], None, {}))
self.assertEqual(spec.is_method, False)
self.assertEqual(spec.input_signature, input_signature)
self.assertEqual(spec.default_values, {'y': 1})
self.assertEqual(
    spec.function_type,
    function_type_lib.FunctionType([
        function_type_lib.Parameter(
            'self', function_type_lib.Parameter.POSITIONAL_OR_KEYWORD,
            False, type_constraint[0]),
        function_type_lib.Parameter(
            'x', function_type_lib.Parameter.POSITIONAL_OR_KEYWORD, False,
            type_constraint[1]),
        function_type_lib.Parameter(
            'y', function_type_lib.Parameter.POSITIONAL_OR_KEYWORD, True,
            type_constraint[2])
    ]))
