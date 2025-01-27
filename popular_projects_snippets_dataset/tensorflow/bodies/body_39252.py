# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_xent_op_test.py
# Warm in
for _ in range(20):
    sess.run(ops)

# Timing run
start = time.time()
for _ in range(20):
    sess.run(ops)
end = time.time()

exit((end - start) / 20.0)  # Average runtime per iteration
