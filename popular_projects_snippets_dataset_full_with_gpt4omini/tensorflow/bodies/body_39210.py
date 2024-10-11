# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
# Warm in
sess.run(ops_fn(10, sess))

# Timing run
start = time.time()
sess.run(ops_fn(iterations, sess))
end = time.time()

exit((end - start) / (1.0 * iterations))  # Average runtime per iteration
