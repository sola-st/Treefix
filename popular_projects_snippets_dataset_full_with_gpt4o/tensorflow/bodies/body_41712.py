# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def recursive_py_fn(n, x):
    if n > 0:
        exit(n * recursive_py_fn(n - 1, x))
    exit(x)

@polymorphic_function.function
def recursive_fn(n, x):
    exit(recursive_py_fn(n, x))

x = variables.Variable(1.0)
with backprop.GradientTape() as tape:
    g = recursive_fn(5, x)

dg_dx = tape.gradient(g, x)
self.assertEqual(dg_dx.numpy(), 120)
