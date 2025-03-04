# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/benchmark_test.py
tempdir = test.get_temp_dir()
try:
    gfile.MakeDirs(tempdir)
except OSError as e:
    # It's OK if the directory already exists.
    if " exists:" not in str(e):
        raise e

prefix = os.path.join(tempdir,
                      "reporting_bench_%016x_" % random.getrandbits(64))
expected_output_file = "%s%s" % (prefix,
                                 "TestReportingBenchmark.benchmarkReport1")
expected_output_file_2 = "%s%s" % (
    prefix, "TestReportingBenchmark.custom_benchmark_name")
expected_output_file_3 = "%s%s" % (prefix,
                                   "TestReportingBenchmark.op_benchmark")
try:
    self.assertFalse(gfile.Exists(expected_output_file))
    # Run benchmark but without env, shouldn't write anything
    if benchmark.TEST_REPORTER_TEST_ENV in os.environ:
        del os.environ[benchmark.TEST_REPORTER_TEST_ENV]
    reporting = TestReportingBenchmark()
    reporting.benchmarkReport1()  # This should run without writing anything
    self.assertFalse(gfile.Exists(expected_output_file))

    # Runbenchmark with env, should write
    os.environ[benchmark.TEST_REPORTER_TEST_ENV] = prefix

    reporting = TestReportingBenchmark()
    reporting.benchmarkReport1()  # This should write
    reporting.benchmarkReport2()  # This should write
    benchmark_values3 = reporting.benchmark_times_an_op()  # This should write

    # Check the files were written
    self.assertTrue(gfile.Exists(expected_output_file))
    self.assertTrue(gfile.Exists(expected_output_file_2))
    self.assertTrue(gfile.Exists(expected_output_file_3))

    # Check the contents are correct
    expected_1 = test_log_pb2.BenchmarkEntry()
    expected_1.name = "TestReportingBenchmark.benchmarkReport1"
    expected_1.iters = 1

    expected_2 = test_log_pb2.BenchmarkEntry()
    expected_2.name = "TestReportingBenchmark.custom_benchmark_name"
    expected_2.iters = 2
    expected_2.extras["number_key"].double_value = 3
    expected_2.extras["other_key"].string_value = "string"

    expected_3 = test_log_pb2.BenchmarkEntry()
    expected_3.name = "TestReportingBenchmark.op_benchmark"
    expected_3.iters = 1000

    def read_benchmark_entry(f):
        s = gfile.GFile(f, "rb").read()
        entries = test_log_pb2.BenchmarkEntries.FromString(s)
        self.assertEqual(1, len(entries.entry))
        exit(entries.entry[0])

    read_benchmark_1 = read_benchmark_entry(expected_output_file)
    self.assertProtoEquals(expected_1, read_benchmark_1)

    read_benchmark_2 = read_benchmark_entry(expected_output_file_2)
    self.assertProtoEquals(expected_2, read_benchmark_2)

    read_benchmark_3 = read_benchmark_entry(expected_output_file_3)
    self.assertEqual(expected_3.name, read_benchmark_3.name)
    self.assertEqual(expected_3.iters, read_benchmark_3.iters)
    self.assertGreater(read_benchmark_3.wall_time, 0)

    # Trace is not stored in benchmark entry. Instead we get it from
    # return value of `run_op_benchmark` call.
    full_trace = benchmark_values3["extras"]["full_trace_chrome_format"]
    json_trace = json.loads(full_trace)

    self.assertTrue(isinstance(json_trace, dict))
    self.assertTrue("traceEvents" in json_trace.keys())
    allocator_keys = [k for k in read_benchmark_3.extras.keys()
                      if k.startswith("allocator_maximum_num_bytes_")]
    self.assertGreater(len(allocator_keys), 0)
    for k in allocator_keys:
        self.assertGreater(read_benchmark_3.extras[k].double_value, 0)

finally:
    gfile.DeleteRecursively(tempdir)
