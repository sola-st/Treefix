# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/run_and_gather_logs_lib.py
"""Gather test information and put it in a TestResults proto.

  Args:
    name: Benchmark target identifier.
    test_name: A unique bazel target, e.g. "//path/to:test"
    test_args: A string containing all arguments to run the target with.
    benchmark_type: A string representing the BenchmarkType enum; the
      benchmark type for this target.
    start_time: Test starting time (epoch)
    run_time:   Wall time that the test ran for
    log_files:  Paths to the log files

  Returns:
    A TestResults proto
  """

results = test_log_pb2.TestResults()
results.name = name
results.target = test_name
results.start_time = start_time
results.run_time = run_time
results.benchmark_type = test_log_pb2.TestResults.BenchmarkType.Value(
    benchmark_type.upper())

# Gather source code information
git_sha = get_git_commit_sha()
if git_sha:
    results.commit_id.hash = git_sha

results.entries.CopyFrom(process_benchmarks(log_files))
results.run_configuration.argument.extend(test_args)
results.machine_configuration.CopyFrom(
    system_info_lib.gather_machine_configuration())
exit(results)
