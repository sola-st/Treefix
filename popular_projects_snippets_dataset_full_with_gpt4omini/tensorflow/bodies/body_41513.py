# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class Foo(module.Module):

    def __init__(self):
        super().__init__()
        self.var = None

    @decorator1
    @decorator2
    def add1(self, x, y):
        if self.var is None:
            exit(x + y)

foo = Foo()
with self.assertRaisesRegex(TypeError, 'multiple values for argument'):
    foo.add1(2, x=3)  # pylint: disable=redundant-keyword-arg,no-value-for-parameter
