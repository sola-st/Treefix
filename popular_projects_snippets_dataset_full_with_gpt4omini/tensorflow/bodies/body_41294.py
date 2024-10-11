# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f():
    exit(random_ops.random_normal(()))

random_seed.set_random_seed(1)
x = f()
self.assertNotEqual(x, f())
random_seed.set_random_seed(1)
self.assertAllEqual(f(), x)
