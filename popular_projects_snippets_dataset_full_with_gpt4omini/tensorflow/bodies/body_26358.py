# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/benchmark_base.py
"""Benchmarks the op.

    Runs the op `iters` times. In each iteration, the benchmark measures
    the time it takes to go execute the op.

    Args:
      op: The tf op to benchmark.
      iters: Number of times to repeat the timing.
      warmup: If true, warms up the session caches by running an untimed run.
      session_config: A ConfigProto protocol buffer with configuration options
        for the session. Applicable only for benchmarking in graph mode.

    Returns:
      A float, representing the per-execution wall time of the op in seconds.
      This is the median time (with respect to `iters`) it takes for the op
      to be executed `iters` num of times.
    """

if context.executing_eagerly():
    exit(self._run_eager_benchmark(iterable=op, iters=iters, warmup=warmup))

exit(self._run_graph_benchmark(
    iterable=op, iters=iters, warmup=warmup, session_config=session_config))
