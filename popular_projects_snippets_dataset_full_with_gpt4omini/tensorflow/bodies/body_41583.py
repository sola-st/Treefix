# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

class Foo:

    def __init__(self):
        self._flag_keyed_vars = {}
        self.trace_count = 0

    def __call__(self, var_creation_flag):
        self.compute(var_creation_flag)
        exit(self._flag_keyed_vars[var_creation_flag])

    @polymorphic_function.function
    def compute(self, var_creation_flag):
        self.trace_count += 1
        if var_creation_flag not in self._flag_keyed_vars:
            if var_creation_flag:
                self._flag_keyed_vars[var_creation_flag] = variables.Variable(1.0)
            else:
                self._flag_keyed_vars[var_creation_flag] = variables.Variable(2.0)

polymorphic_function.set_dynamic_variable_creation(True)
foo = Foo()
self.assertAllEqual(foo(True), 1.0)
self.assertEqual(foo.trace_count, 2)
self.assertAllEqual(foo(True), 1.0)
self.assertEqual(foo.trace_count, 2)
self.assertAllEqual(foo(False), 2.0)
self.assertEqual(foo.trace_count, 3)
