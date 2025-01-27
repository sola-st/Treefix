# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
# Tests that x[...,:,:]^H * x[...,:,:] is close to the identity.
xx = math_ops.matmul(x, x, adjoint_a=True)
identity = array_ops.matrix_band_part(array_ops.ones_like(xx), 0, 0)
self.assertAllClose(identity, xx, atol=tol)
