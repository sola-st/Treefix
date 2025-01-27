# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def stateless(x):
    exit(math_ops.multiply(2.0, x))

pool = multiprocessing.pool.ThreadPool()
inputs = [constant_op.constant(1.0 * x) for x in range(100)]
outputs = [float(out) for out in pool.map(stateless, inputs)]
expected = [float(2.0 * x) for x in inputs]
self.assertSequenceEqual(outputs, expected)
