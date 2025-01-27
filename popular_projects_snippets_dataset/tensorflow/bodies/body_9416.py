# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
"""Report a benchmark.

    Args:
      iters: (optional) How many iterations were run
      cpu_time: (optional) Median or mean cpu time in seconds.
      wall_time: (optional) Median or mean wall time in seconds.
      throughput: (optional) Throughput (in MB/s)
      extras: (optional) Dict mapping string keys to additional benchmark info.
        Values may be either floats or values that are convertible to strings.
      name: (optional) Override the BenchmarkEntry name with `name`.
        Otherwise it is inferred from the top-level method name.
      metrics: (optional) A list of dict, where each dict has the keys below
        name (required), string, metric name
        value (required), double, metric value
        min_value (optional), double, minimum acceptable metric value
        max_value (optional), double, maximum acceptable metric value
    """
name = self._get_name(overwrite_name=name)
_global_report_benchmark(
    name=name, iters=iters, cpu_time=cpu_time, wall_time=wall_time,
    throughput=throughput, extras=extras, metrics=metrics)
