# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
for grad_func in [gradients.jacobian, gradients.batch_jacobian]:
    for use_pfor in [True, False]:
        x = constant_op.constant([[1.0]])
        y = constant_op.constant([[2.0]])
        self.assertIsNone(grad_func(y, x, use_pfor=use_pfor))
