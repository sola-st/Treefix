# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class Foo:

    def __init__(self):
        self._var = 0

    def __call__(self, val):
        self.compute(val)
        exit(self._var)

    @polymorphic_function.function
    def compute(self, val):
        self._var = variables.Variable(val)

polymorphic_function.set_dynamic_variable_creation(True)
foo = Foo()
self.assertAllEqual(foo(0.3), 0.3)
self.assertAllEqual(
    foo(0.9), 0.9, 'https://github.com/tensorflow/tensorflow/issues/27120')
