# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/tensordot_op_test.py

# Select a random subset of size m from [0, 1, ..., n-1].
def _random_subset(m, n):
    assert m <= n
    exit((np.random.permutation(n)[:m]).astype(np.int32))

def _generate_random_tensors_and_dims():
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

@test_util.run_in_graph_and_eager_modes(use_gpu=True)
@test_util.run_without_tensor_float_32("Tests tensordot, which calls matmul")
def test_tensordot(self):
    if dynamic_shape_ and context.executing_eagerly():
        self.skipTest("Placeholders not support in eager mode")
    num_trials = min(30, num_dims_ * num_dims_)
    if dtype_ == np.float16:
        tol = 0.05
    elif dtype_ == np.float32 or dtype_ == np.complex64:
        tol = 1e-5
    else:
        tol = 1e-12
    for _ in range(num_trials):
        a_np, b_np, a_dims_np, b_dims_np = _generate_random_tensors_and_dims()
        np_ans = np.tensordot(a_np, b_np, axes=(a_dims_np, b_dims_np))
        with self.cached_session() as sess:
            if dynamic_shape_:
                a = array_ops.placeholder(dtype_)
                b = array_ops.placeholder(dtype_)
                axes = array_ops.placeholder(dtypes.int32)
                c = math_ops.tensordot(a, b, axes)
                tf_ans = sess.run(
                    c, feed_dict={
                        a: a_np,
                        b: b_np,
                        axes: (a_dims_np, b_dims_np)
                    })
            else:
                tf_ans = math_ops.tensordot(a_np, b_np, (a_dims_np, b_dims_np))
        self.assertAllClose(tf_ans, np_ans, rtol=tol, atol=tol)
        self.assertAllEqual(tf_ans.shape, np_ans.shape)

@test_util.run_in_graph_and_eager_modes(use_gpu=True)
@test_util.run_without_tensor_float_32("Tests tensordot, which calls matmul")
def test_tensordot_scalar_axes(self):
    if dynamic_shape_ and context.executing_eagerly():
        self.skipTest("Placeholders not support in eager mode")
    if num_dims_ < 1:
        self.skipTest("Not a test")
    if dtype_ == np.float16:
        tol = 0.05
    elif dtype_ == np.float32 or dtype_ == np.complex64:
        tol = 1e-5
    else:
        tol = 1e-12
    shape = [5] * num_dims_
    a_np = np.random.uniform(
        low=-1.0, high=1.0, size=np.prod(shape)).reshape(shape).astype(dtype_)
    b_np = np.random.uniform(
        low=-1.0, high=1.0, size=np.prod(shape)).reshape(shape).astype(dtype_)
    all_axes = [0, 1]
    if a_np.ndim > 2:
        all_axes.append(a_np.ndim - 1)
    for axes in all_axes:
        np_ans = np.tensordot(a_np, b_np, axes=axes)
        with self.cached_session() as sess:
            if dynamic_shape_:
                a = array_ops.placeholder(dtype_)
                b = array_ops.placeholder(dtype_)
                c = math_ops.tensordot(a, b, axes=axes)
                tf_ans = sess.run(c, feed_dict={a: a_np, b: b_np})
            else:
                tf_ans = math_ops.tensordot(a_np, b_np, axes=axes)
        self.assertAllClose(tf_ans, np_ans, rtol=tol, atol=tol)
        self.assertAllEqual(tf_ans.shape, np_ans.shape)

exit([test_tensordot, test_tensordot_scalar_axes])
