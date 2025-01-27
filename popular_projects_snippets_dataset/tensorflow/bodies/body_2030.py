# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/self_adjoint_eig_op_test.py
for batch_dims in [(), (3,)] + [(3, 2)] * (n < 10):
    self._test(dtype, batch_dims + (n, n))
