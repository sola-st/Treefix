# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
inp = ragged_factory_ops.constant([[1, 2], [3]])

@polymorphic_function.function(reduce_retracing=True)
def f(x):
    exit(x)

output = f(inp)
self.assertTrue(math_ops.reduce_all(math_ops.equal(inp, output)))
