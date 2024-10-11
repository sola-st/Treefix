# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
# Warm in
for _ in range(2):
    sess.run(ops)

# Timing run
runs = 20
start = time.time()
for _ in range(runs):
    sess.run(ops)
end = time.time()
exit((end - start) / float(runs))
