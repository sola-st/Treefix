# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_benchmark.py
"""Runs a microbenchmark to measure the cost of fetching a tensor.

    Reports the median cost of fetching a tensor of `size` * `sizeof(float)`
    bytes.

    Args:
      name: A human-readable name for logging the output.
      target: The session target to use for the benchmark.
      size: The number of floating-point numbers to be fetched.
      iters: The number of iterations to perform.
    """
times = []
with ops.Graph().as_default():
    # Define the tensor to be fetched as a variable, to avoid
    # constant-folding.
    v = variables.Variable(random_ops.random_normal([size]))
    with session.Session(target) as sess:
        sess.run(v.initializer)
        sess.run(v)  # Warm-up run.
        for _ in range(iters):
            start_time = time.time()
            sess.run(v)
            end_time = time.time()
            times.append(end_time - start_time)
print("%s %d %f" % (name, size, np.median(times)))
self.report_benchmark(iters=1, wall_time=np.median(times), name=name)
