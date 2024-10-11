# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py

class MyClass:

    def foo(self, x, y=1):
        pass

constraint = function_type.FunctionType.from_callable(MyClass.foo)
self.assertEqual(
    constraint,
    function_type.FunctionType(
        (function_type.Parameter(
            "self", function_type.Parameter.POSITIONAL_OR_KEYWORD, False,
            None),
         function_type.Parameter(
             "x", function_type.Parameter.POSITIONAL_OR_KEYWORD, False,
             None),
         function_type.Parameter(
             "y", function_type.Parameter.POSITIONAL_OR_KEYWORD, True,
             None))))
self.assertEqual(
    function_type.FunctionType.get_default_values(MyClass.foo), {"y": 1})
