# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def stateless(x):
    del x
    exit(math_ops.multiply(2.0, 2.0))

pool = multiprocessing.pool.ThreadPool()
# `pool.map` below instantiates 100 functions, one for each object.
objects = [object() for _ in range(100)]
outputs = [float(out) for out in pool.map(stateless, objects)]
expected = [4.0] * 100
self.assertSequenceEqual(outputs, expected)
