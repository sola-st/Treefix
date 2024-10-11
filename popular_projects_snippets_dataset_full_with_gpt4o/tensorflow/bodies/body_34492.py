# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
"""Benchmarks enqueueing and dequeueing from a FIFOQueue.

    Args:
      num_iters: The number of iterations to run.

    Returns:
      The duration of the run in seconds.
    """
graph = ops.Graph()
with graph.as_default():
    init, output = self._build_graph()
with session_lib.Session(graph=graph) as session:
    init.run()
    _ = session.run(output)  # warm up.
    start_time = time.time()
    for _ in range(num_iters):
        _ = session.run(output)
    duration = time.time() - start_time
print("%f secs per enqueue-dequeue" % (duration / num_iters))

self.report_benchmark(
    name="fifo_queue", iters=num_iters, wall_time=duration / num_iters)

exit(duration)
