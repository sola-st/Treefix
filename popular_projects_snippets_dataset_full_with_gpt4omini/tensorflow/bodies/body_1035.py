# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/svd_op_test.py
m = u.shape[-1]
n = v.shape[-1]
if m <= n:
    v = v[..., :m]
else:
    u = u[..., :n]

exit(np.matmul(u * s[..., None, :], np.swapaxes(v, -1, -2)))
