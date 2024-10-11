# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
if is_single:
    atol = 5e-4
else:
    atol = 5e-14
# We only compare the first 'rank' orthogonal vectors since the
# remainder form an arbitrary orthonormal basis for the
# (row- or column-) null space, whose exact value depends on
# implementation details. Notice that since we check that the
# matrices of singular vectors are unitary elsewhere, we do
# implicitly test that the trailing vectors of x and y span the
# same space.
x = x[..., 0:rank]
y = y[..., 0:rank]
# Q is only unique up to sign (complex phase factor for complex matrices),
# so we normalize the sign first.
sum_of_ratios = np.sum(np.divide(y, x), -2, keepdims=True)
phases = np.divide(sum_of_ratios, np.abs(sum_of_ratios))
x *= phases
self.assertAllClose(x, y, atol=atol)
