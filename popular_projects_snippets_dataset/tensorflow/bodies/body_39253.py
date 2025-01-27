# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test.py
config = config_pb2.ConfigProto()
config.allow_soft_placement = True
config.gpu_options.per_process_gpu_memory_fraction = 0.3
labels = np.random.randint(num_entries, size=batch_size).astype(np.int32)
logits = np.random.randn(batch_size, num_entries).astype(np.float32)

def _timer(sess, ops):
    # Warm in
    for _ in range(20):
        sess.run(ops)

    # Timing run
    start = time.time()
    for _ in range(20):
        sess.run(ops)
    end = time.time()

    exit((end - start) / 20.0)  # Average runtime per iteration

# Using sparse_to_dense and softmax_cross_entropy_with_logits
with session.Session(config=config) as sess:
    if not use_gpu:
        with ops_lib.device("/cpu:0"):
            ops = _sparse_vs_dense_xent_benchmark_dense(labels, logits)
    else:
        ops = _sparse_vs_dense_xent_benchmark_dense(labels, logits)
    delta_dense = _timer(sess, ops)

# Using sparse_softmax_cross_entropy_with_logits
with session.Session(config=config) as sess:
    if not use_gpu:
        with test_util.device("/cpu:0"):
            ops = _sparse_vs_dense_xent_benchmark_sparse(labels, logits)
    else:
        ops = _sparse_vs_dense_xent_benchmark_sparse(labels, logits)
    delta_sparse = _timer(sess, ops)

print("%d \t %d \t %s \t %f \t %f \t %f" % (batch_size, num_entries, use_gpu,
                                            delta_dense, delta_sparse,
                                            delta_sparse / delta_dense))
