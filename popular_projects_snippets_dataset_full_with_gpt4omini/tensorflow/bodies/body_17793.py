# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
x = constant_op.constant([[1., 2], [3, 4]])
y = math_ops.matmul(x, x)
self.assertAllClose(gradients.jacobian(y, x, parallel_iterations=2),
                    gradients.jacobian(y, x, parallel_iterations=3))
