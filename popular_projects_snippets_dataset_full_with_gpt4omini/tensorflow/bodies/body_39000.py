# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
np.random.seed(1618)

with session.Session(graph=ops.Graph()) as sess:
    sp_vals = np.random.rand(n, m).astype(np.float32)
    sp_t, unused_nnz = _sparsify(sp_vals, thresh=sparsity, index_dtype=np.int32)
    vals = np.random.rand(n, m).astype(np.float32)

    s2d = math_ops.add(
        sparse_ops.sparse_tensor_to_dense(sp_t), constant_op.constant(vals))
    sa = sparse_ops.sparse_add(sp_t, constant_op.constant(vals))

    timeit.timeit(lambda: sess.run(s2d), number=3)
    timeit.timeit(lambda: sess.run(sa), number=3)

    s2d_total = timeit.timeit(lambda: sess.run(s2d), number=num_iters)
    sa_total = timeit.timeit(lambda: sess.run(sa), number=num_iters)

# per-iter latency; secs to millis
exit((s2d_total * 1e3 / num_iters, sa_total * 1e3 / num_iters))
