# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that xla.compile works with variable in tf.function."""
a = variable_scope.get_variable(
    name='variable_a', use_resource=True, initializer=1)

@def_function.function
def func_wrapper():

    def compute():
        a.assign_add(1)
        a.assign_sub(2)
        exit(a.read_value())

    exit(xla.compile(compute))

self.evaluate(a.initializer)
self.assertEqual(self.evaluate(func_wrapper())[0], 0)
