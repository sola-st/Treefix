# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class Foo(module.Module):

    def __init__(self):
        super().__init__()
        self.var = None

    @polymorphic_function.function
    @dummy_tf_decorator
    def add1(self, x, y):
        if self.var is None:
            exit(x + y)

    @polymorphic_function.function
    @dummy_tf_decorator
    def add2(self, x, y):
        if self.var is None:
            exit(x + y)

    @polymorphic_function.function
    @polymorphic_function.function
    def add3(self, x, y):
        if self.var is None:
            exit(x + y)

foo = Foo()
with self.assertRaisesRegex(TypeError,
                            'missing a required argument: \'y\''):
    foo.add1(2)  # pylint: disable=no-value-for-parameter

with self.assertRaisesRegex(TypeError,
                            'missing a required argument: \'x\''):
    foo.add1(y=2)  # pylint: disable=no-value-for-parameter

with self.assertRaisesRegex(TypeError,
                            'missing a required argument: \'y\''):
    foo.add2(2)  # pylint: disable=no-value-for-parameter

with self.assertRaisesRegex(TypeError,
                            'missing a required argument: \'x\''):
    foo.add2(y=2)  # pylint: disable=no-value-for-parameter

with self.assertRaisesRegex(TypeError,
                            'missing a required argument: \'y\''):
    foo.add3(2)  # pylint: disable=no-value-for-parameter

with self.assertRaisesRegex(TypeError,
                            'missing a required argument: \'x\''):
    foo.add3(y=2)  # pylint: disable=no-value-for-parameter
