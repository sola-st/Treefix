# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

integer = constant_op.constant(2, dtypes.int64)

class Foo:

    @polymorphic_function.function
    def func(self, other=integer):
        exit(other)

foo = Foo()
self.assertEqual(foo.func().numpy(), int(integer))
