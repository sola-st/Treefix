# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
if is_single:
    tol = 1e-5
else:
    tol = 1e-14
# Tests that a ~= q*r.
a_recon = test_util.matmul_without_tf32(q, r)
self.assertAllClose(a_recon, a, rtol=tol, atol=tol)
