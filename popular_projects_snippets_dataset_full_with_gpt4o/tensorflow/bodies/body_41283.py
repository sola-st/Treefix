# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

v = resource_variable_ops.ResourceVariable(1.0)

@polymorphic_function.function
def stateful(x):
    v.assign(x)

pool = multiprocessing.pool.ThreadPool()
inputs = [constant_op.constant(0.0)] * 100
pool.map(stateful, inputs)
self.assertEqual(float(v.read_value()), 0.0)
