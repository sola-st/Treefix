# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_benchmark.py
"""Runs a microbenchmark to measure the cost of running an op.

    Reports the median cost of running a trivial (Variable) op.

    Args:
      name: A human-readable name for logging the output.
      target: The session target to use for the benchmark.
      iters: The number of iterations to perform.
    """
times = []
with ops.Graph().as_default():
    # Define the op to be run as a variable, to avoid
    # constant-folding.
    v = variables.Variable(random_ops.random_normal([]))
    with session.Session(target) as sess:
        sess.run(v.initializer)
        sess.run(v.op)  # Warm-up run.
        for _ in range(iters):
            start_time = time.time()
            sess.run(v.op)
            end_time = time.time()
            times.append(end_time - start_time)
print("%s %f" % (name, np.median(times)))
self.report_benchmark(iters=1, wall_time=np.median(times), name=name)
