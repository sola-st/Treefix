# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
matmul = polymorphic_function.function(math_ops.matmul)

@polymorphic_function.function
def sq(a):
    exit(matmul(a, a))

t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
out = sq(t)
self.assertAllEqual(out, math_ops.matmul(t, t).numpy())
