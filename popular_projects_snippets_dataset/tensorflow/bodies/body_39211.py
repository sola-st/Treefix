# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
config = config_pb2.ConfigProto()
config.allow_soft_placement = True

# Configurable for benchmarking:
# config.intra_op_parallelism_threads = 100
# config.gpu_options.per_process_gpu_memory_fraction = 0.3

np.random.seed([6, 117])  # Reproducibility
x = np.random.rand(m, k).astype(np.float32)
x[x < thresh] = 0
y = np.random.randn(k, n).astype(np.float32)
if adjoint_a:
    x = x.T
if adjoint_b:
    y = y.T

def _timer(sess, ops_fn, iterations):
    # Warm in
    sess.run(ops_fn(10, sess))

    # Timing run
    start = time.time()
    sess.run(ops_fn(iterations, sess))
    end = time.time()

    exit((end - start) / (1.0 * iterations))  # Average runtime per iteration

# Using regular matmul, marking one of the matrices as dense.
if skip_dense:
    delta_dense = float("nan")
else:
    with session.Session(config=config, graph=ops.Graph()) as sess:
        if not use_gpu:
            with ops.device("/cpu:0"):
                x_t = constant_op.constant(x)
                y_t = constant_op.constant(y)
                ops_fn = _sparse_tensor_dense_vs_dense_matmul_benchmark_dense(
                    x_t, y_t, adjoint_a, adjoint_b)
        else:
            with ops.device("/device:GPU:0"):
                x_t = constant_op.constant(x)
                y_t = constant_op.constant(y)
                ops_fn = _sparse_tensor_dense_vs_dense_matmul_benchmark_dense(
                    x_t, y_t, adjoint_a, adjoint_b)
        delta_dense = _timer(sess, ops_fn, 200)

  # Using sparse_tensor_dense_matmul.
with session.Session("", config=config, graph=ops.Graph()) as sess:
    if not use_gpu:
        with ops.device("/cpu:0"):
            x_ind = constant_op.constant(np.vstack(np.where(x)).astype(np.int64).T)
            x_val = constant_op.constant(x[np.where(x)])
            x_shape = constant_op.constant(np.array(x.shape).astype(np.int64))
            y_t = constant_op.constant(y)
            ops_fn = _sparse_tensor_dense_vs_dense_matmul_benchmark_sparse(
                x_ind, x_val, x_shape, y_t, adjoint_a, adjoint_b)
    else:
        with ops.device("/device:GPU:0"):
            x_ind = constant_op.constant(np.vstack(np.where(x)).astype(np.int64).T)
            x_val = constant_op.constant(x[np.where(x)])
            x_shape = constant_op.constant(np.array(x.shape).astype(np.int64))
            y_t = constant_op.constant(y)
            ops_fn = _sparse_tensor_dense_vs_dense_matmul_benchmark_sparse(
                x_ind, x_val, x_shape, y_t, adjoint_a, adjoint_b)
    delta_sparse = _timer(sess, ops_fn, 200)

print("%g \t %d \t %s \t %d \t %d \t %g \t %g \t %g" %
      (1 - thresh, n, use_gpu, m, k, delta_dense, delta_sparse,
       delta_sparse / delta_dense))
