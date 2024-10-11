# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
# Tests that x[...,:,:]^H * x[...,:,:] is close to the identity.
xx = test_util.matmul_without_tf32(x, x, adjoint_a=True)
identity = array_ops.matrix_band_part(array_ops.ones_like(xx), 0, 0)
if is_single:
    tol = 1e-5
else:
    tol = 1e-14
self.assertAllClose(identity, xx, atol=tol)
