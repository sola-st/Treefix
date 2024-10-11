# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
add = lambda x, y: x + y**2
add = polymorphic_function.function(experimental_implements='MyFunc')(add)
x = variables.Variable(3.0)
y = variables.Variable(2.0)

with backprop.GradientTape() as tape:
    g = add(x, y)

dg_dy, dg_dx = tape.gradient(g, [y, x])
self.assertEqual(dg_dy.numpy(), 4.0)
self.assertEqual(dg_dx.numpy(), 1.0)
