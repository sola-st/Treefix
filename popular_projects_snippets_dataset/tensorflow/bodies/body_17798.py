# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
x = constant_op.constant([[1., 2], [3, 4]])
w = constant_op.constant([[1., 2, 3, 4], [5, 6, 7, 8]])
y = math_ops.matmul(x, w)
self.assertAllClose(gradients.batch_jacobian(y, x, parallel_iterations=2),
                    gradients.batch_jacobian(y, x, parallel_iterations=3))
