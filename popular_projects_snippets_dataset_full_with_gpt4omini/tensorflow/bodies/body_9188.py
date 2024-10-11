# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler_test.py
output_dir = test.get_temp_dir()
run_metadata = config_pb2.RunMetadata()
graph = test.mock.MagicMock()
graph.get_operations.return_value = []

profiles = pprof_profiler.get_profiles(graph, run_metadata)
self.assertEqual(0, len(profiles))
profile_files = pprof_profiler.profile(
    graph, run_metadata, output_dir)
self.assertEqual(0, len(profile_files))
