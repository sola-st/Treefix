# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_benchmark.py
"""Runs a microbenchmark to measure the cost of feeding a tensor.

    Reports the median cost of feeding a tensor of `size` * `sizeof(float)`
    bytes.

    Args:
      name: A human-readable name for logging the output.
      target: The session target to use for the benchmark.
      size: The number of floating-point numbers to be feed.
      iters: The number of iterations to perform.
    """
feed_val = np.random.rand(size).astype(np.float32)
times = []
with ops.Graph().as_default():
    p = array_ops.placeholder(dtypes.float32, shape=[size])
    # Fetch the operation rather than the tensor, to avoid measuring the time
    # to fetch back the value.
    no_op = array_ops.identity(p).op
    with session.Session(target) as sess:
        sess.run(no_op, feed_dict={p: feed_val})  # Warm-up run.
        for _ in range(iters):
            start_time = time.time()
            sess.run(no_op, feed_dict={p: feed_val})
            end_time = time.time()
            times.append(end_time - start_time)
print("%s %d %f" % (name, size, np.median(times)))
self.report_benchmark(iters=1, wall_time=np.median(times), name=name)
