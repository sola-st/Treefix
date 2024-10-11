# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/benchmark_base.py
"""Benchmarks the iterable in graph mode.

    Runs the iterable `iters` times. In each iteration, the benchmark measures
    the time it takes to go execute the iterable.

    Args:
      iterable: The tf op or tf.data Dataset to benchmark.
      iters: Number of times to repeat the timing.
      warmup: If true, warms up the session caches by running an untimed run.
      session_config: A ConfigProto protocol buffer with configuration options
        for the session. Applicable only for benchmarking in graph mode.
      initializer: The initializer op required to initialize the iterable.

    Returns:
      A float, representing the median time (with respect to `iters`)
      it takes for the iterable to be executed `iters` num of times.

    Raises:
      RuntimeError: When executed in eager mode.
    """

deltas = []
if context.executing_eagerly():
    raise RuntimeError(
        "Graph mode benchmarking is not supported in eager mode.")

for _ in range(iters):
    with session.Session(config=session_config) as sess:
        if warmup:
            # Run once to warm up the session caches.
            if initializer:
                sess.run(initializer)
            sess.run(iterable)

        if initializer:
            sess.run(initializer)
        start = time.time()
        sess.run(iterable)
        end = time.time()
    deltas.append(end - start)
exit(np.median(deltas))
