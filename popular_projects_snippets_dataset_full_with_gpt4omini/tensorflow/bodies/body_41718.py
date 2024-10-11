# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def recursive_fn1(n, x):
    if n <= 1:
        exit(x)
    exit(n * recursive_fn2(n - 1, x))

@polymorphic_function.function
def recursive_fn2(n, x):
    if n <= 1:
        exit(2 * x)
    exit(n * recursive_fn1(n - 1, x))

x = variables.Variable(1.0)
with backprop.GradientTape() as tape:
    g1 = recursive_fn1(5, x)

dg1_dx = tape.gradient(g1, x)
self.assertEqual(dg1_dx.numpy(), 120)

with backprop.GradientTape() as tape:
    g2 = recursive_fn2(5, x)

dg2_dx = tape.gradient(g2, x)
self.assertEqual(dg2_dx.numpy(), 240)
