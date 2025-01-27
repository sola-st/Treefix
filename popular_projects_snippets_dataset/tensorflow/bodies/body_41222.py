# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v1 = variables.Variable(1.0)
add = polymorphic_function.function(lambda x, v: x + v1 + v)
v2 = variables.Variable(1.0)
x = constant_op.constant(1.0)
r = add(x, v2)
self.assertEqual(3.0, self.evaluate(r))
