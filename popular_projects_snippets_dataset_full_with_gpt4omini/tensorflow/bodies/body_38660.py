# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/tensordot_op_test.py
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
