# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py

def foo(x, y=2):  # pylint: disable=unused-argument
    pass

constraint = function_type.FunctionType.from_callable(foo)
constraint.bind(*(1, 2))
constraint.bind(*(), **{"x": 1, "y": 2})
constraint.bind(*(1,), **{"y": 2})
constraint.bind(*(1,))
constraint.bind(*(), **{"x": 1})

with self.assertRaisesRegex(TypeError, "too many positional arguments"):
    constraint.bind(*(1, 2, 3))

with self.assertRaisesRegex(TypeError, "multiple values for argument 'x'"):
    constraint.bind(*(1,), **{"x": 2})

with self.assertRaisesRegex(TypeError,
                            "got an unexpected keyword argument 'z'"):
    constraint.bind(*(1, 2), **{"z": 2})

with self.assertRaisesRegex(TypeError, "missing a required argument: 'x'"):
    constraint.bind(*(), **{"z": 3})
