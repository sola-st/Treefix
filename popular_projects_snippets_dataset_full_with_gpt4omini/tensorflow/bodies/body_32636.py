# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_grad_test.py
with self.cached_session():
    batch_size = constant_op.constant(3)
    matrix_size = constant_op.constant(4)
    batch_identity = array_ops.tile(
        array_ops.expand_dims(
            array_ops.diag(array_ops.ones([matrix_size])), 0),
        [batch_size, 1, 1])
    determinants = linalg_ops.matrix_determinant(batch_identity)
    reduced = math_ops.reduce_sum(determinants)
    sum_grad = gradients_impl.gradients(reduced, batch_identity)[0]
    self.assertAllClose(batch_identity, self.evaluate(sum_grad))
