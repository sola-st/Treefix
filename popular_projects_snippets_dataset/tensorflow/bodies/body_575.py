# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/run_and_gather_logs_lib.py
"""Run the bazel test given by test_name.  Gather and return the logs.

  Args:
    name: Benchmark target identifier.
    test_name: A unique bazel target, e.g. "//path/to:test"
    test_args: A string containing all arguments to run the target with.
    benchmark_type: A string representing the BenchmarkType enum; the
      benchmark type for this target.
    skip_processing_logs: Whether to skip processing test results from log
      files.

  Returns:
    A tuple (test_results, mangled_test_name), where
    test_results: A test_log_pb2.TestResults proto, or None if log processing
      is skipped.
    test_adjusted_name: Unique benchmark name that consists of
      benchmark name optionally followed by GPU type.

  Raises:
    ValueError: If the test_name is not a valid target.
    subprocess.CalledProcessError: If the target itself fails.
    IOError: If there are problems gathering test log output from the test.
    MissingLogsError: If we couldn't find benchmark logs.
  """
if not (test_name and test_name.startswith("//") and ".." not in test_name and
        not test_name.endswith(":") and not test_name.endswith(":all") and
        not test_name.endswith("...") and len(test_name.split(":")) == 2):
    raise ValueError("Expected test_name parameter with a unique test, e.g.: "
                     "--test_name=//path/to:test")
test_executable = test_name.rstrip().strip("/").replace(":", "/")

if gfile.Exists(os.path.join("bazel-bin", test_executable)):
    # Running in standalone mode from core of the repository
    test_executable = os.path.join("bazel-bin", test_executable)
else:
    # Hopefully running in sandboxed mode
    test_executable = os.path.join(".", test_executable)

test_adjusted_name = name
gpu_config = gpu_info_lib.gather_gpu_devices()
if gpu_config:
    gpu_name = gpu_config[0].model
    gpu_short_name_match = re.search(
        r"(Tesla|NVIDIA) (K40|K80|P100|V100|A100)", gpu_name
    )
    if gpu_short_name_match:
        gpu_short_name = gpu_short_name_match.group(0)
        test_adjusted_name = name + "|" + gpu_short_name.replace(" ", "_")

temp_directory = tempfile.mkdtemp(prefix="run_and_gather_logs")
mangled_test_name = (
    test_adjusted_name.strip("/").replace("|",
                                          "_").replace("/",
                                                       "_").replace(":", "_"))
test_file_prefix = os.path.join(temp_directory, mangled_test_name)
test_file_prefix = "%s." % test_file_prefix

try:
    if not gfile.Exists(test_executable):
        test_executable_py3 = test_executable + ".python3"
        if not gfile.Exists(test_executable_py3):
            raise ValueError("Executable does not exist: %s" % test_executable)
        test_executable = test_executable_py3
    test_args = shlex.split(test_args)

    # This key is defined in tf/core/util/reporter.h as
    # TestReporter::kTestReporterEnv.
    os.environ["TEST_REPORT_FILE_PREFIX"] = test_file_prefix
    start_time = time.time()
    subprocess.check_call([test_executable] + test_args)
    if skip_processing_logs:
        exit((None, test_adjusted_name))
    run_time = time.time() - start_time
    log_files = gfile.Glob("{}*".format(test_file_prefix))
    if not log_files:
        raise MissingLogsError("No log files found at %s." % test_file_prefix)

    exit((process_test_logs(
        test_adjusted_name,
        test_name=test_name,
        test_args=test_args,
        benchmark_type=benchmark_type,
        start_time=int(start_time),
        run_time=run_time,
        log_files=log_files), test_adjusted_name))

finally:
    try:
        gfile.DeleteRecursively(temp_directory)
    except OSError:
        pass
