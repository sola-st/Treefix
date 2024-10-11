# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler_test.py
output_dir = test.get_temp_dir()
run_metadata = config_pb2.RunMetadata()

node1 = step_stats_pb2.NodeExecStats(
    node_name='Add/123',
    op_start_rel_micros=3,
    op_end_rel_micros=5,
    all_end_rel_micros=4)

run_metadata = config_pb2.RunMetadata()
device1 = run_metadata.step_stats.dev_stats.add()
device1.device = 'deviceA'
device1.node_stats.extend([node1])

graph = test.mock.MagicMock()
op1 = test.mock.MagicMock()
op1.name = 'Add/123'
op1.traceback = [
    ('a/b/file1', 10, 'apply_op', 'abc'), ('a/c/file2', 12, 'my_op', 'def')]
op1.type = 'add'
graph.get_operations.return_value = [op1]

expected_proto = """sample_type {
  type: 5
  unit: 5
}
sample_type {
  type: 6
  unit: 7
}
sample_type {
  type: 8
  unit: 7
}
sample {
  value: 1
  value: 4
  value: 2
  label {
    key: 1
    str: 2
  }
  label {
    key: 3
    str: 4
  }
}
string_table: ""
string_table: "node_name"
string_table: "Add/123"
string_table: "op_type"
string_table: "add"
string_table: "count"
string_table: "all_time"
string_table: "nanoseconds"
string_table: "op_time"
string_table: "Device 1 of 1: deviceA"
comment: 9
"""
# Test with protos
profiles = pprof_profiler.get_profiles(graph, run_metadata)
self.assertEqual(1, len(profiles))
self.assertTrue('deviceA' in profiles)
self.assertEqual(expected_proto, str(profiles['deviceA']))
# Test with files
profile_files = pprof_profiler.profile(
    graph, run_metadata, output_dir)
self.assertEqual(1, len(profile_files))
with gzip.open(profile_files[0]) as profile_file:
    profile_contents = profile_file.read()
    profile = profile_pb2.Profile()
    profile.ParseFromString(profile_contents)
    self.assertEqual(expected_proto, str(profile))
