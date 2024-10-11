# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = variables.Variable(1.0)
add = polymorphic_function.function(lambda x: x.assign_add(1.0))
r1 = add(v)
self.assertEqual(2.0, self.evaluate(r1))
c = constant_op.constant(1.0)
with self.assertRaisesRegex(AttributeError, 'no attribute'):
    add(c)
