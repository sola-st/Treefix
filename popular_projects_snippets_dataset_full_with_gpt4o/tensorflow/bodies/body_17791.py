# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
# Shape x: [3, 4]
x = random_ops.random_uniform([3, 4])
_, y = tf_control_flow_ops.while_loop(lambda i, a: i > 5.,
                                      lambda i, a: (i + 1, a + i),
                                      (constant_op.constant(0.), x))
# Shape y: [2, 3]
y = y[:2, :3]
jacobian = gradients.jacobian(y, x)

expected_shape = [2, 3, 3, 4]
self.assertAllEqual(expected_shape, jacobian.shape.as_list())
