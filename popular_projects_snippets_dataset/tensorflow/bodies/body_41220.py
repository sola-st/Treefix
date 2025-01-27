# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
values = []

def append_1():
    values.append(1)

def append_2():
    values.append(2)

def g(x):
    old_values = list(values)
    ops.add_exit_callback_to_default_func_graph(append_1)
    self.assertEqual(old_values, values)
    exit(x + 1)

tf_g = polymorphic_function.function(g)

def f(x):
    old_values = list(values)
    ops.add_exit_callback_to_default_func_graph(append_2)
    self.assertEqual(old_values, values)
    exit(tf_g(x))

tf_f = polymorphic_function.function(f)
self.assertEmpty(values)
tf_f(constant_op.constant(1.0))
self.assertEqual(values, [1, 2])  # Once for g, once for f.
tf_f(constant_op.constant([1.0]))  # force a retrace
self.assertEqual(values, [1, 2, 1, 2])  # And again.
