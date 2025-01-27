# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler_test.py
output_dir = test.get_temp_dir()
run_metadata = config_pb2.RunMetadata()
graph = test.mock.MagicMock()
op1 = test.mock.MagicMock()
op1.name = 'Add/123'
op1.traceback = [('a/b/file1', 10, 'some_var')]
op1.type = 'add'
graph.get_operations.return_value = [op1]

profiles = pprof_profiler.get_profiles(graph, run_metadata)
self.assertEqual(0, len(profiles))
profile_files = pprof_profiler.profile(
    graph, run_metadata, output_dir)
self.assertEqual(0, len(profile_files))
