# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
"""Method for recording a benchmark directly.

  Args:
    name: The BenchmarkEntry name.
    iters: (optional) How many iterations were run
    cpu_time: (optional) Total cpu time in seconds
    wall_time: (optional) Total wall time in seconds
    throughput: (optional) Throughput (in MB/s)
    extras: (optional) Dict mapping string keys to additional benchmark info.
    metrics: (optional) A list of dict representing metrics generated by the
      benchmark. Each dict should contain keys 'name' and'value'. A dict
      can optionally contain keys 'min_value' and 'max_value'.

  Raises:
    TypeError: if extras is not a dict.
    IOError: if the benchmark output file already exists.
  """
logging.info("Benchmark [%s] iters: %d, wall_time: %g, cpu_time: %g,"
             "throughput: %g, extras: %s, metrics: %s", name,
             iters if iters is not None else -1,
             wall_time if wall_time is not None else -1,
             cpu_time if cpu_time is not None else -1,
             throughput if throughput is not None else -1,
             str(extras) if extras else "None",
             str(metrics) if metrics else "None")

entries = test_log_pb2.BenchmarkEntries()
entry = entries.entry.add()
entry.name = name
if iters is not None:
    entry.iters = iters
if cpu_time is not None:
    entry.cpu_time = cpu_time
if wall_time is not None:
    entry.wall_time = wall_time
if throughput is not None:
    entry.throughput = throughput
if extras is not None:
    if not isinstance(extras, dict):
        raise TypeError("extras must be a dict")
    for (k, v) in extras.items():
        if isinstance(v, numbers.Number):
            entry.extras[k].double_value = v
        else:
            entry.extras[k].string_value = str(v)
if metrics is not None:
    if not isinstance(metrics, list):
        raise TypeError("metrics must be a list")
    for metric in metrics:
        if "name" not in metric:
            raise TypeError("metric must has a 'name' field")
        if "value" not in metric:
            raise TypeError("metric must has a 'value' field")

        metric_entry = entry.metrics.add()
        metric_entry.name = metric["name"]
        metric_entry.value = metric["value"]
        if "min_value" in metric:
            metric_entry.min_value.value = metric["min_value"]
        if "max_value" in metric:
            metric_entry.max_value.value = metric["max_value"]

test_env = os.environ.get(TEST_REPORTER_TEST_ENV, None)
if test_env is None:
    # Reporting was not requested, just print the proto
    print(str(entries))
    exit()

serialized_entry = entries.SerializeToString()

mangled_name = name.replace("/", "__")
output_path = "%s%s" % (test_env, mangled_name)
if gfile.Exists(output_path):
    raise IOError("File already exists: %s" % output_path)
with gfile.GFile(output_path, "wb") as out:
    out.write(serialized_entry)
