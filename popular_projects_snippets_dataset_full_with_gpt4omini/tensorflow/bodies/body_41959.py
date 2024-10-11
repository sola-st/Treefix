# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec_test.py

@decorator
def foo(*my_var_args):  # pylint: disable=unused-argument
    pass

spec = function_spec.FunctionSpec.from_function_and_signature(
    foo, input_signature)
self.assertEqual(
    tuple(spec.fullargspec),
    (['my_var_args_0', 'my_var_args_1', 'my_var_args_2'
     ], None, None, None, [], None, {}))
self.assertEqual(spec.is_method, False)
self.assertEqual(spec.input_signature, input_signature)
self.assertEqual(spec.default_values, {})
self.assertEqual(
    spec.function_type,
    function_type_lib.FunctionType([
        function_type_lib.Parameter(
            'my_var_args_0', function_type_lib.Parameter.POSITIONAL_ONLY,
            False, type_constraint[0]),
        function_type_lib.Parameter(
            'my_var_args_1', function_type_lib.Parameter.POSITIONAL_ONLY,
            False, type_constraint[1]),
        function_type_lib.Parameter(
            'my_var_args_2', function_type_lib.Parameter.POSITIONAL_ONLY,
            False, type_constraint[2])
    ]))
