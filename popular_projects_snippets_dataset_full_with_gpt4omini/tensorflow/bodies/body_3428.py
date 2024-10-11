# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py

def foo(x, y, z=3):  # pylint: disable=unused-argument
    pass

constraint = function_type.FunctionType.from_callable(foo)
self.assertEqual(
    constraint,
    function_type.FunctionType(
        (function_type.Parameter(
            "x", function_type.Parameter.POSITIONAL_OR_KEYWORD, False,
            None),
         function_type.Parameter(
             "y", function_type.Parameter.POSITIONAL_OR_KEYWORD, False,
             None),
         function_type.Parameter(
             "z", function_type.Parameter.POSITIONAL_OR_KEYWORD, True,
             None))))
self.assertEqual(
    function_type.FunctionType.get_default_values(foo), {"z": 3})
