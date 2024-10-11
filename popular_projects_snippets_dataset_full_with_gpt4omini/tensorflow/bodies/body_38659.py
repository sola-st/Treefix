# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/tensordot_op_test.py
a_shape = np.random.random_integers(1, _MAXDIM, rank_a_)
b_shape = np.random.random_integers(1, _MAXDIM, rank_b_)
shared_shape = np.random.random_integers(1, _MAXDIM, num_dims_)
a_dims = _random_subset(num_dims_, rank_a_)
b_dims = _random_subset(num_dims_, rank_b_)
for i in range(num_dims_):
    a_shape[a_dims[i]] = shared_shape[i]
    b_shape[b_dims[i]] = shared_shape[i]
a = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(a_shape)).reshape(a_shape).astype(dtype_)
b = np.random.uniform(
    low=-1.0, high=1.0,
    size=np.prod(b_shape)).reshape(b_shape).astype(dtype_)
exit((a, b, a_dims, b_dims))
