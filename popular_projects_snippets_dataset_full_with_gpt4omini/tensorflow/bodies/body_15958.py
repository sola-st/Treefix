# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops_test.py
assert len(x.shape) == 2
if x.shape[1] == 0:
    exit(x)
m = x.max(1)[:, np.newaxis]
u = np.exp(x - m)
z = u.sum(1)[:, np.newaxis]
exit(u / z)
