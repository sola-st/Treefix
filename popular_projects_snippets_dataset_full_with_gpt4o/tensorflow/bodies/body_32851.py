# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
if not use_static_shape_ and context.executing_eagerly():
    exit()
is_complex = dtype_ in (np.complex64, np.complex128)
is_single = dtype_ in (np.float32, np.complex64)
tol = 3e-4 if is_single else 1e-12
if test.is_gpu_available():
    # The gpu version returns results that are much less accurate.
    tol *= 200
np.random.seed(42)
x_np = np.random.uniform(
    low=-1.0, high=1.0, size=np.prod(shape_)).reshape(shape_).astype(dtype_)
if is_complex:
    x_np += 1j * np.random.uniform(
        low=-1.0, high=1.0,
        size=np.prod(shape_)).reshape(shape_).astype(dtype_)

if use_static_shape_:
    x_tf = constant_op.constant(x_np)
else:
    x_tf = array_ops.placeholder(dtype_)

if compute_uv_:
    s_tf, u_tf, v_tf = linalg_ops.svd(
        x_tf, compute_uv=compute_uv_, full_matrices=full_matrices_)
    if use_static_shape_:
        s_tf_val, u_tf_val, v_tf_val = self.evaluate([s_tf, u_tf, v_tf])
    else:
        with self.session() as sess:
            s_tf_val, u_tf_val, v_tf_val = sess.run([s_tf, u_tf, v_tf],
                                                    feed_dict={x_tf: x_np})
else:
    s_tf = linalg_ops.svd(
        x_tf, compute_uv=compute_uv_, full_matrices=full_matrices_)
    if use_static_shape_:
        s_tf_val = self.evaluate(s_tf)
    else:
        with self.session() as sess:
            s_tf_val = sess.run(s_tf, feed_dict={x_tf: x_np})

if compute_uv_:
    u_np, s_np, v_np = np.linalg.svd(
        x_np, compute_uv=compute_uv_, full_matrices=full_matrices_)
else:
    s_np = np.linalg.svd(
        x_np, compute_uv=compute_uv_, full_matrices=full_matrices_)
# We explicitly avoid the situation where numpy eliminates a first
# dimension that is equal to one.
s_np = np.reshape(s_np, s_tf_val.shape)

CompareSingularValues(self, s_np, s_tf_val, tol)
if compute_uv_:
    CompareSingularVectors(self, u_np, u_tf_val, min(shape_[-2:]), tol)
    CompareSingularVectors(self, np.conj(np.swapaxes(v_np, -2, -1)), v_tf_val,
                           min(shape_[-2:]), tol)
    CheckApproximation(self, x_np, u_tf_val, s_tf_val, v_tf_val,
                       full_matrices_, tol)
    CheckUnitary(self, u_tf_val, tol)
    CheckUnitary(self, v_tf_val, tol)
