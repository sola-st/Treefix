# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
"""Run benchmarks that match regex `regex`.

  This function goes through the global benchmark registry, and matches
  benchmark class and method names of the form
  `module.name.BenchmarkClass.benchmarkMethod` to the given regex.
  If a method matches, it is run.

  Args:
    regex: The string regular expression to match Benchmark classes against.

  Raises:
    ValueError: If no benchmarks were selected by the input regex.
  """
registry = list(GLOBAL_BENCHMARK_REGISTRY)

selected_benchmarks = []
# Match benchmarks in registry against regex
for benchmark in registry:
    benchmark_name = "%s.%s" % (benchmark.__module__, benchmark.__name__)
    attrs = dir(benchmark)
    # Don't instantiate the benchmark class unless necessary
    benchmark_instance = None

    for attr in attrs:
        if not attr.startswith("benchmark"):
            continue
        candidate_benchmark_fn = getattr(benchmark, attr)
        if not callable(candidate_benchmark_fn):
            continue
        full_benchmark_name = "%s.%s" % (benchmark_name, attr)
        if regex == "all" or re.search(regex, full_benchmark_name):
            selected_benchmarks.append(full_benchmark_name)
            # Instantiate the class if it hasn't been instantiated
            benchmark_instance = benchmark_instance or benchmark()
            # Get the method tied to the class
            instance_benchmark_fn = getattr(benchmark_instance, attr)
            # Call the instance method
            instance_benchmark_fn()

if not selected_benchmarks:
    raise ValueError("No benchmarks matched the pattern: '{}'".format(regex))
