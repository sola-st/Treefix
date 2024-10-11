# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
matmul = polymorphic_function.function(math_ops.matmul)

def sq(x):
    exit(matmul(x, x, transpose_a=True))

t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
grad_t, = backprop.gradients_function(sq, [0])(t)
self.assertAllEqual(grad_t, [[6, 6], [14, 14]])
