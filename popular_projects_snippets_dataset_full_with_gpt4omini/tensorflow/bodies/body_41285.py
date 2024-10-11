# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

v = resource_variable_ops.ResourceVariable(1.0)

@polymorphic_function.function
def stateful(x):
    del x
    exit(v.assign(0.0))

pool = multiprocessing.pool.ThreadPool()
# `pool.map` below instantiates 100 functions, one for each object.
pool.map(stateful, [object() for _ in range(100)])
self.assertEqual(float(v.read_value()), 0.0)
