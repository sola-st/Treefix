# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
x = constant_op.constant([1.]).gpu()
f = polymorphic_function.function(math_ops.add)
y = f(x, x).cpu()
self.assertAllEqual(y, [2.])
