# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark_test.py
output_dir = self.get_temp_dir() + os.path.sep
os.environ['TEST_REPORT_FILE_PREFIX'] = output_dir
proto_file_path = os.path.join(output_dir,
                               'BenchmarkTest.testReportBenchmark')
if os.path.exists(proto_file_path):
    os.remove(proto_file_path)

self.report_benchmark(
    iters=2000,
    wall_time=1000,
    name='testReportBenchmark',
    metrics=[{'name': 'metric_name_1', 'value': 0, 'min_value': 1},
             {'name': 'metric_name_2', 'value': 90, 'min_value': 0,
              'max_value': 95}])

with open(proto_file_path, 'rb') as f:
    benchmark_entries = test_log_pb2.BenchmarkEntries()
    benchmark_entries.ParseFromString(f.read())

    actual_result = json_format.MessageToDict(
        benchmark_entries, preserving_proto_field_name=True,
        including_default_value_fields=True)['entry'][0]
os.remove(proto_file_path)

expected_result = {
    'name': 'BenchmarkTest.testReportBenchmark',
    # google.protobuf.json_format.MessageToDict() will convert
    # int64 field to string.
    'iters': '2000',
    'wall_time': 1000,
    'cpu_time': 0,
    'throughput': 0,
    'extras': {},
    'metrics': [
        {
            'name': 'metric_name_1',
            'value': 0,
            'min_value': 1
        },
        {
            'name': 'metric_name_2',
            'value': 90,
            'min_value': 0,
            'max_value': 95
        }
    ]
}

self.assertEqual(2000, benchmark_entries.entry[0].iters)
self.assertDictEqual(expected_result, actual_result)
