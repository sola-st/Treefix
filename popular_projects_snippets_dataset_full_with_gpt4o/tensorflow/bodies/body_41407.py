# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

integer = constant_op.constant(2, dtypes.int64)

class Foo:

    def one(self, tensor):
        exit(tensor)

    @polymorphic_function.function
    def two(self, tensor, other=integer):
        exit((self.one(tensor), other))

foo = Foo()
t = constant_op.constant(1.0)
one, two = foo.two(t)
self.assertEqual(one.numpy(), 1.0)
self.assertEqual(two.numpy(), 2)
