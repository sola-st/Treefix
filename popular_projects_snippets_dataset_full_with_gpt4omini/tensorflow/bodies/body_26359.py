# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/benchmark_base.py
"""Benchmarks the dataset.

    Runs the dataset `iters` times. In each iteration, the benchmark measures
    the time it takes to go through `num_elements` elements of the dataset.

    Args:
      dataset: Dataset to benchmark.
      num_elements: Number of dataset elements to iterate through each benchmark
        iteration.
      iters: Number of times to repeat the timing.
      warmup: If true, warms up the session caches by running an untimed run.
      apply_default_optimizations: Determines whether default optimizations
        should be applied.
      session_config: A ConfigProto protocol buffer with configuration options
        for the session. Applicable only for benchmarking in graph mode.

    Returns:
      A float, representing the per-element wall time of the dataset in seconds.
      This is the median time (with respect to `iters`) it takes for the dataset
      to go through `num_elements` elements, divided by `num_elements.`
    """

# The options that have been applied to the dataset are preserved so that
# they are not overwritten while benchmarking.
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = (
    apply_default_optimizations)
dataset = dataset.with_options(options)

# NOTE: We use `dataset.skip()` to perform the iterations in C++, avoiding
# the overhead of having to execute a TensorFlow op for each step of the
# input pipeline. Note that this relies on the underlying implementation of
# `skip` to execute upstream computation. If it is optimized in the future,
# we will have to change this code.
dataset = dataset.skip(num_elements - 1)

if context.executing_eagerly():
    median_duration = self._run_eager_benchmark(
        iterable=dataset, iters=iters, warmup=warmup)
    exit(median_duration / float(num_elements))

iterator = dataset_ops.make_initializable_iterator(dataset)
next_element = iterator.get_next()
op = nest.flatten(next_element)[0].op
median_duration = self._run_graph_benchmark(
    iterable=op,
    iters=iters,
    warmup=warmup,
    session_config=session_config,
    initializer=iterator.initializer)
exit(median_duration / float(num_elements))
