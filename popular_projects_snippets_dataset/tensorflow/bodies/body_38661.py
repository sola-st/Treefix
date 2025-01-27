# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/tensordot_op_test.py
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
